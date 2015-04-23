from django.shortcuts import render_to_response
from django.shortcuts import render
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

from django.http import HttpResponseRedirect
from django.http import HttpResponse
from blog.models import NewsList
from blog.models import AddLinkForm
from blog.models import ShowNewsList
from blog.models import UserInfo
from blog.models import LoginForm
from blog.models import RegisterForm
from crawler.article2db import article2db
from django.template import RequestContext, loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# from django.contrib.sessions.models import Session

import random
import datetime
import time
# import alchemyapi

@login_required(login_url='login/')
def index(request):
    username = request.user.username
    art = article2db()
    # print username
    if UserInfo.objects.exists():
        userInfo = UserInfo.objects.get(Username=username)
    else:
        userInfo = UserInfo(Username=username)
        userInfo.save()
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AddLinkForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            url = form.cleaned_data['LinkName']
            art.put_url(url)
            
        userInfo.TravelWeight= userInfo.TravelWeight+0.1
        userInfo.save()
        return HttpResponseRedirect('index.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AddLinkForm()    
        keylist = art.list_all_key()
        keylist = keylist[:5]

        news_list = []
        for key in keylist:
            news = art.retrieve_news(key)
            news_to_render = ShowNewsList()
            news_to_render.theme = news['title']
            news_to_render.text = news['text'][0:200] +"..."
            news_to_render.author =news['author']
            news_to_render.day = '19'
            news_to_render.month = 'April'
            news_to_render.keywords = news['keywords']
            news_to_render.weblinks = news['url']
            news_list.append(news_to_render)
        template = loader.get_template('index.html')
        context = RequestContext(request, {
            'latest_news_list': news_list,
            'form': form,
            'userInfo':userInfo,
        })
        return HttpResponse(template.render(context))



def login_user(request):
    # return render_to_response("login.html")
    if request.user.is_authenticated():
        return redirect(reverse('index'))
    errors = ''
    form = LoginForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            user = form.login(request)
            if user:
                login(request, user)
                return redirect(reverse('index'))
        errors='Sorry, that login was invalid. Please try again.'
    #     return redirect(reverse('login'))
    # else:  # GET methods
    template = loader.get_template('login.html')
    context = RequestContext(request, {
        'form': form,
        'errors':errors,
    })
    return HttpResponse(template.render(context))
        # return render_to_response("login.html", {'errors': errors}, RequestContext(request))

def register(request):
    if request.user.is_authenticated():
        return redirect(reverse('index'))
    errors = ''
    username = None
    email = None
    password1 = None
    password2 = None
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username'] 
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            email = form.cleaned_data['email']
        if not username or not email or not password1 or not password2 or password1 != password2:
            errors='Regiser information is not correct, please register again!'
        if not errors:
            try:
                user = User.objects.create_user(username, email, password1)
                user.save()
                userInfo = UserInfo(Username=username)
                userInfo.save()
                return redirect(reverse('login'))
            except Exception as ex:
                errors='User already exists, please register again!'
    form = RegisterForm()   
    template = loader.get_template('register.html')
    context = RequestContext(request, {
        'form': form,
        'errors': errors,
    })
    return HttpResponse(template.render(context))
    # return render_to_response("register.html", RequestContext(request))

@login_required
def logout_user(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return render_to_response('logout.html')
    # return redirect(reverse('login'))
