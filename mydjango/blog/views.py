from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from blog.models import ContactPost
from blog.models import UserProfile
from blog.models import UserData
from blog.models import ContactForm
from blog.models import RegisterForm
from blog.models import LoginForm
from blog.models import UserControlForm
from blog.models import NewsList
from blog.models import NameForm
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
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
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
            # print res
            item=NewsList(theme=title,text=text,author=author,weblinks=url,keywords=res)
            item.save()
        return HttpResponseRedirect('index.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()    
        userInfo = UserInfo()
        news_list = NewsList.objects.order_by('-pub_date')
        news_list = news_list[0:5]
        latest_news_list = []
        for news in news_list:
            news_to_render = ShowNewsList()
            news_to_render.theme = news.theme
            news_to_render.text = news.text[1:200] +"..."
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
        # if request.session.get('logflag', False):
        #     navigation_link1 = 'user_control.html'
        #     navigation_label1 = request.session.get('username')
        #     navigation_link2 = 'logout.html'
        #     navigation_label2 = 'Logout'
        #                 # return HttpResponse('You are logged in')
        #     # return render_to_response('index.html', locals())
        # else:
        #     navigation_link1 = 'login.html'
        #     navigation_label1 = 'Login'
        #     navigation_link2 = 'register.html'
        #     navigation_label2 = 'Register'
        #
        # # sometexts = 'You can replace all this text with your own text.'
        
        # data = {'sometexts', 'You can replace all this text with your own text.'}
        # return render_to_response('index.html',data)
        
        # return render_to_response('index.html', {
#             'navigation_label1': navigation_label1,
#             'navigation_link1': navigation_link1,
#             'navigation_label2': navigation_label2,
#             'navigation_link2': navigation_link2,
#         },
#         context_instance=RequestContext(request))
            # return render_to_response('index.html', locals())
    
def contact(request):
    
    if request.session.get('logflag', False):
        navigation_link1 = 'user_control.html'
        navigation_label1 = request.session.get('username')
        navigation_link2 = 'logout.html'
        navigation_label2 = 'Logout'
                    # return HttpResponse('You are logged in')
        # return render_to_response('index.html', locals())
    else:
        navigation_link1 = 'login.html'
        navigation_label1 = 'Login'
        navigation_link2 = 'register.html'
        navigation_label2 = 'Register'
    
    if request.method == 'GET':
        form = ContactForm() # An unbound form

        return render_to_response('contact.html', {
            'navigation_label1': navigation_label1,
            'navigation_link1': navigation_link1,
            'navigation_label2': navigation_label2,
            'navigation_link2': navigation_link2,
            'form': form,
        },
        context_instance=RequestContext(request))
        
        # return render_to_response('contact.html', locals())
    elif request.method == 'POST':
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid():
            Subject = form.cleaned_data['Subject']
            Name = form.cleaned_data['Name']
            Email = form.cleaned_data['Email']
            Message = form.cleaned_data['Message']
            Recipients = ['jzrw2009@gmail.com']
            tmp = ContactPost(Name= Name, Email=Email, Subject= Subject, Message= Message) 
            tmp.save()
            # if cc_myself:
            #     recipients.append(sender)

            from django.core.mail import send_mail
            send_mail(Subject, Message, Email, Recipients)
            return HttpResponseRedirect('/index.html') # Redirect after POST
            
        return render_to_response('contact.html', {
            'navigation_label1': navigation_label1,
            'navigation_link1': navigation_link1,
            'navigation_label2': navigation_label2,
            'navigation_link2': navigation_link2,
            'form': form,
        },
        context_instance=RequestContext(request))

    
def register(request):
    if request.session.get('logflag', False):
        navigation_link1 = 'user_control.html'
        navigation_label1 = request.session.get('username')
        navigation_link2 = 'logout.html'
        navigation_label2 = 'Logout'
                    # return HttpResponse('You are logged in')
        # return render_to_response('index.html', locals())
    else:
        navigation_link1 = 'login.html'
        navigation_label1 = 'Login'
        navigation_link2 = 'register.html'
        navigation_label2 = 'Register'
        
    if request.method == 'GET':
        form = RegisterForm() # An unbound form
        return render_to_response('register.html', {
            'form': form,
            'navigation_label1': navigation_label1,
            'navigation_link1': navigation_link1,
            'navigation_label2': navigation_label2,
            'navigation_link2': navigation_link2,
        },
        context_instance=RequestContext(request))
        # return render_to_response('contact.html', locals())
    elif request.method == 'POST':
        form = RegisterForm(request.POST) # A form bound to the POST data
        if form.is_valid():            
            StationNum = form.cleaned_data['StationNum']
            Username = form.cleaned_data['Username']
            OldPassword = form.cleaned_data['OldPassword']
            NewPassword = form.cleaned_data['NewPassword']
            ReEnterPassword = form.cleaned_data['ReEnterPassword']
            Firstname = form.cleaned_data['Firstname']
            Lastname = form.cleaned_data['Lastname']
            Email = form.cleaned_data['Email']
            User.objects.create_user(Username,Email,NewPassword)  
            tmp = UserProfile(StationNum= StationNum, Firstname= Firstname, Lastname= Lastname, Email= Email, Username=Username) 
            tmp.save()
            return HttpResponseRedirect('register_success.html') # Redirect after POST

    return render_to_response('register.html', {
        'form': form,
        'navigation_label1': navigation_label1,
        'navigation_link1': navigation_link1,
        'navigation_label2': navigation_label2,
        'navigation_link2': navigation_link2,
    },
    context_instance=RequestContext(request))    
    
def login(request):
    if request.session.get('logflag', False):
        navigation_link1 = 'user_control.html'
        navigation_label1 = request.session.get('username')
        navigation_link2 = 'logout.html'
        navigation_label2 = 'Logout'
        return render_to_response('user_control.html', {
            'navigation_label1': navigation_label1,
            'navigation_link1': navigation_link1,
            'navigation_label2': navigation_label2,
            'navigation_link2': navigation_link2,
        })
                    # return HttpResponse('You are logged in')
        # return render_to_response('index.html', locals())
    else:
        navigation_link1 = 'login.html'
        navigation_label1 = 'Login'
        navigation_link2 = 'register.html'
        navigation_label2 = 'Register'
    
        if request.method == 'GET':
            form = LoginForm() # An unbound form
            return render(request, 'login.html', {
                'form': form,
                'navigation_label1': navigation_label1,
                'navigation_link1': navigation_link1,
                'navigation_label2': navigation_label2,
                'navigation_link2': navigation_link2,
            })
            # return render_to_response('contact.html', locals())
        elif request.method == 'POST':
            form = LoginForm(request.POST) # A form bound to the POST data
            if form.is_valid():
                UserOrEmail = form.cleaned_data['UserOrEmail']
                Password = form.cleaned_data['Password']
                user = authenticate(username = UserOrEmail, password = Password) 
                if user is not None:
                    request.session['logflag'] = True
                    request.session['username'] = user.get_username()
                    request.session.set_expiry(0) 
                    return HttpResponseRedirect('user_control.html') # Redirect after POST
            
            return render(request, 'login.html', 
            {'form': form,
            'navigation_label1': navigation_label1,
            'navigation_link1': navigation_link1,
            'navigation_label2': navigation_label2,
            'navigation_link2': navigation_link2,
            })    
    

def about(request):
    if request.session.get('logflag', False):
        navigation_link1 = 'user_control.html'
        navigation_label1 = request.session.get('username')
        navigation_link2 = 'logout.html'
        navigation_label2 = 'Logout'
                    # return HttpResponse('You are logged in')
        # return render_to_response('index.html', locals())
    else:
        navigation_link1 = 'login.html'
        navigation_label1 = 'Login'
        navigation_link2 = 'register.html'
        navigation_label2 = 'Register'
        
    return render_to_response('about.html', {
        'navigation_label1': navigation_label1,
        'navigation_link1': navigation_link1,
        'navigation_label2': navigation_label2,
        'navigation_link2': navigation_link2,
    },
    context_instance=RequestContext(request))    

def register_success(request):
    if request.session.get('logflag', False):
        navigation_link1 = 'user_control.html'
        navigation_label1 = request.session.get('username')
        navigation_link2 = 'logout.html'
        navigation_label2 = 'Logout'
                    # return HttpResponse('You are logged in')
        # return render_to_response('index.html', locals())
    else:
        navigation_link1 = 'login.html'
        navigation_label1 = 'Login'
        navigation_link2 = 'register.html'
        navigation_label2 = 'Register'
        
    return render_to_response('register_success.html', {
        'navigation_label1': navigation_label1,
        'navigation_link1': navigation_link1,
        'navigation_label2': navigation_label2,
        'navigation_link2': navigation_link2,
    },
    context_instance=RequestContext(request))   
        
def user_control(request):
    CurrentUsername = request.session.get('username');

    if request.session.get('logflag', False):
        navigation_link1 = 'user_control.html'
        navigation_label1 = CurrentUsername
        navigation_link2 = 'logout.html'
        navigation_label2 = 'Logout'
                    # return HttpResponse('You are logged in')
        # return render_to_response('index.html', locals())
    else:
        navigation_link1 = 'login.html'
        navigation_label1 = 'Login'
        navigation_link2 = 'register.html'
        navigation_label2 = 'Register'
        
    if request.method == 'GET':
        form = UserControlForm() # An unbound form
        return render_to_response('user_control.html', {
            'form': form,
            'navigation_label1': navigation_label1,
            'navigation_link1': navigation_link1,
            'navigation_label2': navigation_label2,
            'navigation_link2': navigation_link2,
        },
        context_instance=RequestContext(request))
        # return render_to_response('contact.html', locals())
    elif request.method == 'POST':
        form = UserControlForm(request.POST) # A form bound to the POST data
        if form.is_valid():            
            NewPassword = form.cleaned_data['NewPassword']
            ReEnterPassword = form.cleaned_data['ReEnterPassword']
            Firstname = form.cleaned_data['Firstname']
            Lastname = form.cleaned_data['Lastname']
            Email = form.cleaned_data['Email']
            # User.objects.create_user(Username,Email,NewPassword)  
    #         tmp = UserProfile(StationNum= StationNum, Firstname= Firstname, Lastname= Lastname, Email= Email, Username=Username) 
    #         tmp.save()
    #         return HttpResponseRedirect('register_success.html') # Redirect after POST

    return render_to_response('user_control.html', {
        'form': form,
        'navigation_label1': navigation_label1,
        'navigation_link1': navigation_link1,
        'navigation_label2': navigation_label2,
        'navigation_link2': navigation_link2,
    },
    context_instance=RequestContext(request))
       
    
def data_viewing(request):
    if request.session.get('logflag', False):
        navigation_link1 = 'user_control.html'
        navigation_label1 = request.session.get('username')
        navigation_link2 = 'logout.html'
        navigation_label2 = 'Logout'
                    # return HttpResponse('You are logged in')
        # return render_to_response('index.html', locals())
    else:
        navigation_link1 = 'login.html'
        navigation_label1 = 'Login'
        navigation_link2 = 'register.html'
        navigation_label2 = 'Register'
        
    xdata = ["Apple", "Apricot", "Avocado", "Banana", "Boysenberries", "Blueberries", "Dates", "Grapefruit", "Kiwi", "Lemon"]
    ydata = [52, 48, 160, 94, 75, 71, 490, 82, 46, 17]
    chartdata = {'x': xdata, 'y': ydata}
    charttype = "pieChart"
    chartcontainer = 'piechart_container'
    data = {
        'navigation_label1': navigation_label1,
        'navigation_link1': navigation_link1,
        'navigation_label2': navigation_label2,
        'navigation_link2': navigation_link2,
        'charttype': charttype,
        'chartdata': chartdata,
        'chartcontainer': chartcontainer,
        'extra': {
            'x_is_date': False,
            'x_axis_format': '',
            'tag_script_js': False,
            'jquery_on_ready': False,
        }
    }
    return render_to_response('data_viewing.html', data)
    
    
def device_management(request):
    if request.session.get('logflag', False):
        navigation_link1 = 'user_control.html'
        navigation_label1 = request.session.get('username')
        navigation_link2 = 'logout.html'
        navigation_label2 = 'Logout'
                    # return HttpResponse('You are logged in')
        # return render_to_response('index.html', locals())
    else:
        navigation_link1 = 'login.html'
        navigation_label1 = 'Login'
        navigation_link2 = 'register.html'
        navigation_label2 = 'Register'
        
    xdata = ["Apple", "Apricot", "Avocado", "Banana", "Boysenberries", "Blueberries", "Dates", "Grapefruit", "Kiwi", "Lemon"]
    ydata = [52, 48, 160, 94, 75, 71, 490, 82, 46, 17]
    chartdata = {'x': xdata, 'y': ydata}
    charttype = "pieChart"
    chartcontainer = 'piechart_container'
    data = {
        'navigation_label1': navigation_label1,
        'navigation_link1': navigation_link1,
        'navigation_label2': navigation_label2,
        'navigation_link2': navigation_link2,
        'charttype': charttype,
        'chartdata': chartdata,
        'chartcontainer': chartcontainer,
        'extra': {
            'x_is_date': False,
            'x_axis_format': '',
            'tag_script_js': False,
            'jquery_on_ready': False,
        }
    }
    return render_to_response('device_management.html', data)        



def logout(request):
    try:
        del request.session['logflag']
    except KeyError:
        pass
    navigation_link1 = 'login.html'
    navigation_label1 = 'Login'
    navigation_link2 = 'register.html'
    navigation_label2 = 'Register'
    return render_to_response('index.html', {
        'navigation_label1': navigation_label1,
        'navigation_link1': navigation_link1,
        'navigation_label2': navigation_label2,
        'navigation_link2': navigation_link2,
    },
    context_instance=RequestContext(request))


    
def news(request):
    if request.session.get('logflag', False):
        navigation_link1 = 'user_control.html'
        navigation_label1 = request.session.get('username')
        navigation_link2 = 'logout.html'
        navigation_label2 = 'Logout'
                    # return HttpResponse('You are logged in')
        # return render_to_response('index.html', locals())
    else:
        navigation_link1 = 'login.html'
        navigation_label1 = 'Login'
        navigation_link2 = 'register.html'
        navigation_label2 = 'Register'
        
    return render_to_response('news.html', {
        'navigation_label1': navigation_label1,
        'navigation_link1': navigation_link1,
        'navigation_label2': navigation_label2,
        'navigation_link2': navigation_link2,
    },
    context_instance=RequestContext(request))
    
    # return render_to_response('news.html', locals())
    
def post(request):
    if request.session.get('logflag', False):
        navigation_link1 = 'user_control.html'
        navigation_label1 = request.session.get('username')
        navigation_link2 = 'logout.html'
        navigation_label2 = 'Logout'
                    # return HttpResponse('You are logged in')
        # return render_to_response('index.html', locals())
    else:
        navigation_link1 = 'login.html'
        navigation_label1 = 'Login'
        navigation_link2 = 'register.html'
        navigation_label2 = 'Register'
        
    return render_to_response('post.html', {
        'navigation_label1': navigation_label1,
        'navigation_link1': navigation_link1,
        'navigation_label2': navigation_label2,
        'navigation_link2': navigation_link2,
    },
    context_instance=RequestContext(request))
    # return render_to_response('post.html', locals())
    
def galleries(request):
    # if request.session.get('logflag', False):
    #     navigation_link1 = 'user_control.html'
    #     navigation_label1 = request.session.get('username')
    #     navigation_link2 = 'logout.html'
    #     navigation_label2 = 'Logout'
    #                 # return HttpResponse('You are logged in')
    #     # return render_to_response('index.html', locals())
    # else:
    #     navigation_link1 = 'login.html'
    #     navigation_label1 = 'Login'
    #     navigation_link2 = 'register.html'
    #     navigation_label2 = 'Register'
    #
    # return render_to_response('galleries.html', {
    #     'navigation_label1': navigation_label1,
    #     'navigation_link1': navigation_link1,
    #     'navigation_label2': navigation_label2,
    #     'navigation_link2': navigation_link2,
    # },
    # context_instance=RequestContext(request))
    return render_to_response('galleries.html')
    
  
    