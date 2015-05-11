from django.shortcuts import render_to_response
from django.shortcuts import render
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

from django.http import HttpResponseRedirect
from django.http import HttpResponse
from blog.models import NewsList
from blog.models import AddLinkForm
from blog.models import ShowNewsList
# from blog.models import UserInfo
from blog.models import LoginForm
from blog.models import RegisterForm
from crawler.article2db import article2db
from crawler.userInfo import userInfo

from django.template import RequestContext, loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt,csrf_protect

from django.core.paginator import Paginator, InvalidPage

# from django.contrib.sessions.models import Session

import random
import datetime
import time
import json
# import alchemyapi

@csrf_protect
# @login_required(login_url='login/')
def index(request):
    if request.method == 'POST':
        if request.user.is_authenticated():
            username = request.user.username
            usr = userInfo(username)
            # create a form instance and populate it with data from the request:
            form = AddLinkForm(request.POST)
            # check whether it's valid:
            if form.is_valid():
                url = form.cleaned_data['LinkName']
                usr.set_bookmark(url)
            # if a GET (or any other method) we'll create a blank form
    else:
        form = AddLinkForm()   
        news_list = []        
        if request.user.is_authenticated():
            username = request.user.username
        else:
            username = "anonymous"
        usr = userInfo(username)
        bookmarklist = usr.get_bookmarks()
        for news in bookmarklist[0:6]:
            news_to_render = ShowNewsList()
            news_to_render.theme = news['title']
            news_to_render.text = news['text'][0:200] +"..."
            news_to_render.author =news['author']
            news_to_render.day = '4'
            news_to_render.month = 'May'
            news_to_render.keywords = news['keywords']
            news_to_render.weblinks = news['url']
            news_list.append(news_to_render)
        
        template = loader.get_template('index.html')
        context = RequestContext(request, {
            'object_list': news_list,
            'form': form,
        # 'userInfo':userInfo,
        })
        return HttpResponse(template.render(context))
        
@csrf_protect
def world(request):
    if request.method == 'GET':
        form = AddLinkForm()   
        news_list = []        
        if request.user.is_authenticated():
            username = request.user.username
        else:
            username = "world"
        usr = userInfo(username)
        bookmarklist = usr.get_bookmarks()
        for news in bookmarklist[0:6]:
            news_to_render = ShowNewsList()
            news_to_render.theme = news['title']
            news_to_render.text = news['text'][0:200] +"..."
            news_to_render.author =news['author']
            news_to_render.day = '4'
            news_to_render.month = 'May'
            news_to_render.keywords = news['keywords']
            news_to_render.weblinks = news['url']
            news_list.append(news_to_render)
        
        template = loader.get_template('world.html')
        context = RequestContext(request, {
            'object_list': news_list,
            'form': form,
        # 'userInfo':userInfo,
        })
        return HttpResponse(template.render(context))

@csrf_protect
def entertainment(request):
    if request.method == 'GET':
        form = AddLinkForm()   
        news_list = []        
        if request.user.is_authenticated():
            username = request.user.username
        else:
            username = "entertainment"
        usr = userInfo(username)
        bookmarklist = usr.get_bookmarks()
        for news in bookmarklist[0:6]:
            news_to_render = ShowNewsList()
            news_to_render.theme = news['title']
            news_to_render.text = news['text'][0:200] +"..."
            news_to_render.author =news['author']
            news_to_render.day = '4'
            news_to_render.month = 'May'
            news_to_render.keywords = news['keywords']
            news_to_render.weblinks = news['url']
            news_list.append(news_to_render)
        
        template = loader.get_template('entertainment.html')
        context = RequestContext(request, {
            'object_list': news_list,
            'form': form,
        # 'userInfo':userInfo,
        })
        return HttpResponse(template.render(context))

@csrf_protect
def sport(request):
    if request.method == 'GET':
        form = AddLinkForm()   
        news_list = []        
        if request.user.is_authenticated():
            username = request.user.username
        else:
            username = "sport"
        usr = userInfo(username)
        bookmarklist = usr.get_bookmarks()
        for news in bookmarklist[0:6]:
            news_to_render = ShowNewsList()
            news_to_render.theme = news['title']
            news_to_render.text = news['text'][0:200] +"..."
            news_to_render.author =news['author']
            news_to_render.day = '4'
            news_to_render.month = 'May'
            news_to_render.keywords = news['keywords']
            news_to_render.weblinks = news['url']
            news_list.append(news_to_render)
        
        template = loader.get_template('sport.html')
        context = RequestContext(request, {
            'object_list': news_list,
            'form': form,
        # 'userInfo':userInfo,
        })
        return HttpResponse(template.render(context))

@csrf_exempt
def get_data(request):
    if request.method == 'POST':
        mydata = request.read()
        str_list= mydata.split('&')
        [str1,number]=str_list[0].split('=')
        [str2,offset]=str_list[1].split('=')
        [str3,desc]=str_list[2].split('=')

    if desc =='index':
        usr = userInfo("anonymous")
    else:
        usr = userInfo(desc)
        
    bookmarklist = usr.get_bookmark_scroll(int(number), int(offset))
    data =""
    for news in bookmarklist:
        data += '<li><div class="date"><p><span>' + '4' + '</span>'
        data += 'May'+'</p></div><h2 ><a href='
        data += news['url']+'>'+ news['title']
        data += '</a></h2><p>' +news['text'][0:200] +"..."+'</p></li>'    
    return HttpResponse(data)






# Pull the data
    # usr = userInfo("anonymous")
    # bookmarklist = usr.get_bookmarks()
    # # Pull the proper items for this page
    # paginator = Paginator(bookmarklist, 6)
    # page_obj = paginator.page(2)
    #
    # # Pass out the data
    # context = {
    #     "object_list": page_obj.object_list,
    #     "page": page_obj,
    # }
    # template = loader.get_template('scroll.json')
    # return HttpResponse(template.render(context))
    # if request.is_ajax() or request.method == 'POST':    

@csrf_exempt
def chrome_login(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')

        user = authenticate(username=name, password=password)
        response_data = {}
        if user:
            # login(request, user)
            response_data['result'] = 'success'
        else:
            response_data['result']= 'fail'
            
        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )

@csrf_exempt
def chrome_archive(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')

        user = authenticate(username=name, password=password)
        response_data = {}
        if user:
            # login(request, user)
            response_data['result'] = 'success'
        else:
            response_data['result']= 'fail'
            
        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )

@csrf_exempt
def chrome_todaypick(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')

        user = authenticate(username=name, password=password)
        response_data = {}
        if user:
            # login(request, user)
            response_data['result'] = 'success'
        else:
            response_data['result']= 'fail'
            
        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )

@csrf_exempt
def chrome_bookmark(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')

        user = authenticate(username=name, password=password)
        response_data = {}
        if user:
            # login(request, user)
            response_data['result'] = 'success'
        else:
            response_data['result']= 'fail'
            
        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )        


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
                # userInfo = UserInfo(Username=username)
                # userInfo.save()
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
