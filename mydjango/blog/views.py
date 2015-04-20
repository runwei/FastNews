from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from blog.models import NewsList
from blog.models import AddLinkForm
from blog.models import ShowNewsList
from blog.models import UserInfo
from django.template import RequestContext, loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

# from django.contrib.sessions.models import Session

import random
import datetime
import time
import alchemyapi

@login_required(login_url='login/') 
def index(request):
    username = request.user.username
    print username
    userInfo = UserInfo.objects.get(Username=username)
    if userInfo is None:
        userInfo = UserInfo(Username=username)
        userInfo.save()
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AddLinkForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            url = form.cleaned_data['LinkName']
            # url = form.LinkName
            inst = alchemyapi.AlchemyAPI()
            keywords = inst.keywords("url", url)
            text = inst.text("url",url)
            title = inst.title("url",url)
            author = inst.author("url",url)
            if keywords['status'] == 'ERROR':
                return HttpResponseRedirect('index.html') 
            else:
                keywords = keywords['keywords']
                text = text['text']
                title = title['title']
                author = author['author']
            res = ""
            for item in keywords:
                kws = item ['text']
                kws_list = kws.split(" ")
                for i in kws_list:
                    res = res+i+" "
            item=NewsList(theme=title,text=text,author=author,weblinks=url,keywords=res)
            item.save()
        userInfo.TravelWeight= userInfo.TravelWeight+0.1
        userInfo.save()
        return HttpResponseRedirect('index.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AddLinkForm()    
        news_list = NewsList.objects.order_by('-pub_date')
        news_list = news_list[0:5]
        latest_news_list = []
        for news in news_list:
            news_to_render = ShowNewsList()
            news_to_render.theme = news.theme
            news_to_render.text = news.text[0:200] +"..."
            news_to_render.author =news.author
            if news.pub_date is None:
                news_to_render.day = '19'
                news_to_render.month = 'April'
            else:
                news_to_render.monthday = news.pub_date.date()
                news_to_render.year = news.pub_date.time()
            news_to_render.keywords = news.keywords
            news_to_render.weblinks = news.weblinks
            latest_news_list.append(news_to_render)
        template = loader.get_template('index.html')
        context = RequestContext(request, {
            'latest_news_list': latest_news_list,
            'form': form,
            'userInfo':userInfo,
        })
        return HttpResponse(template.render(context))

    