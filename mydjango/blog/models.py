from django.db import models
from django import forms
# from django.forms.util import ErrorList
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
# import datetime


class ContactPost(models.Model):
    Name = models.CharField(max_length=50)    # EmailField()
    Subject = models.CharField(max_length=100)
    Message = models.CharField(max_length=100)
    Email= models.EmailField()
    Date = models.DateTimeField(auto_now_add=True)

class UserProfile(models.Model):
    StationNum = models.CharField(max_length=10)
    Username = models.CharField(max_length=10)
    Firstname = models.CharField(max_length=15)        
    Lastname = models.CharField(max_length=15)    
    Email = models.EmailField()        
    Updatetime = models.DateTimeField(auto_now_add=True)

class UserData(models.Model):
    DeviceNum = models.CharField(max_length=10)
    DeviceType = models.CharField(max_length=5)
    DataValue = models.FloatField(max_length=10)
    Time = models.DateTimeField(auto_now_add=True)
    
class ContactForm(forms.Form):
    Name = forms.CharField(max_length=100)    # EmailField()
    Email= forms.EmailField()
    Subject = forms.CharField(max_length=100)
    Message = forms.CharField(max_length=100)
    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        Name = cleaned_data.get('Name')
        Email = cleaned_data.get('Email')
        Subject = cleaned_data.get('Subject')
        Message = cleaned_data.get('Message')
        
        # if not Name:
        #     self._errors['Name'] = ErrorList([u"Input your name!"])
        # if not Subject:
        #     self._errors['Subject'] = ErrorList([u"Input the subject!"])
        # if not Message:
        #     self._errors['Message'] = ErrorList([u"Input the message!"])
        # if not Email:
        #     self._errors['Email'] = ErrorList([u"Input the correct email address!"])
        return cleaned_data
  
class LoginForm(forms.Form):
    UserOrEmail= forms.CharField(max_length=75)
    Password = forms.CharField(max_length=100)
    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        UserOrEmail = cleaned_data.get('UserOrEmail')
        Password =  cleaned_data.get('Password')
        if not UserOrEmail:
            UserOrEmail = UserOrEmail
            # self._errors['UserOrEmail'] = ErrorList([u"Input your username or email address!"])
        else:
            user = authenticate(username = UserOrEmail, password = Password) # user = authenticate(username='john', password='secret')
            # if user is None:
                # self._errors['Password'] = ErrorList([u"Username/Email address and password mismatch!"])
        return cleaned_data
        
class RegisterForm(forms.Form):
    StationNum = forms.CharField(max_length=10)
    Username = forms.CharField(max_length=10)
    OldPassword = forms.CharField(max_length=15)
    NewPassword = forms.CharField(max_length=15)
    ReEnterPassword = forms.CharField(max_length=15)
    Firstname = forms.CharField(max_length=15)        
    Lastname = forms.CharField(max_length=15)    
    Email = forms.EmailField()    
    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        StationNum = cleaned_data.get('StationNum')
        Username = cleaned_data.get('Username')
        OldPassword = cleaned_data.get('OldPassword')
        NewPassword = cleaned_data.get('NewPassword')
        ReEnterPassword = cleaned_data.get('ReEnterPassword')
        Firstname = cleaned_data.get('Firstname')      
        Lastname = cleaned_data.get('Lastname')
        Email = cleaned_data.get('Email')
        # u = User.objects.get(username__exact = Username)
        # if not Username:
        #     self._errors['Username'] = ErrorList([u"Username has to be 2-10 characters!"])
        # elif len(Username)< 2:
        #     self._errors['Username'] = ErrorList([u"Username has to be 2-10 characters!"])
        # elif User.objects.filter(username=Username).count():
        #     self._errors['Username'] = ErrorList([u"Username already exists!"])
        # if not StationNum:
        #     self._errors['StationNum'] = ErrorList([u"Input your Station Serial Number!"])
        # if not NewPassword:
        #     self._errors['NewPassword'] = ErrorList([u"Password has to be 5-15 characters!"])
        # elif len(NewPassword)<5:
        #     self._errors['NewPassword'] = ErrorList([u"Password has to be 5-15 characters!"])
        # if NewPassword != ReEnterPassword:
        #     self._errors['ReEnterPassword'] = ErrorList([u"Password mismatch!"])
        # if not Email:
        #     self._errors['Email'] = ErrorList([u"Email format is not correct!"])
        # elif User.objects.filter(email= Email).count():
        #     self._errors['Email'] = ErrorList([u"Email address is already registered!"])

        return cleaned_data

class UserControlForm(forms.Form):
    OldPassword = forms.CharField(max_length=15)
    NewPassword = forms.CharField(max_length=15)
    ReEnterPassword = forms.CharField(max_length=15)
    Firstname = forms.CharField(max_length=15)        
    Lastname = forms.CharField(max_length=15)    
    Email = forms.EmailField()    
    def clean(self):
        cleaned_data = super(UserControlForm, self).clean()
        Username = cleaned_data.get('Username')
        NewPassword = cleaned_data.get('NewPassword')
        ReEnterPassword = cleaned_data.get('ReEnterPassword')
        Firstname = cleaned_data.get('Firstname')      
        Lastname = cleaned_data.get('Lastname')
        Email = cleaned_data.get('Email')
        # u = User.objects.get(username__exact = Username)
        # if not Username:
        #     self._errors['Username'] = ErrorList([u"Username has to be 2-10 characters!"])
        # elif len(Username)< 2:
        #     self._errors['Username'] = ErrorList([u"Username has to be 2-10 characters!"])
        # elif User.objects.filter(username=Username).count():
        #     self._errors['Username'] = ErrorList([u"Username already exists!"])
        # if not NewPassword:
        #     self._errors['NewPassword'] = ErrorList([u"Password has to be 5-15 characters!"])
        # elif len(NewPassword)<5:
        #     self._errors['NewPassword'] = ErrorList([u"Password has to be 5-15 characters!"])
        # if NewPassword != ReEnterPassword:
        #     self._errors['ReEnterPassword'] = ErrorList([u"Password mismatch!"])
        # if not Email:
        #     self._errors['Email'] = ErrorList([u"Email format is not correct!"])
        # elif User.objects.filter(email= Email).count():
        #     self._errors['Email'] = ErrorList([u"Email address is already registered!"])

        return cleaned_data

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class NewsList(models.Model):
    theme = models.CharField(max_length=200)
    text = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published',blank=True, null=True)
    keywords = models.CharField(max_length=200)
    weblinks = models.CharField(max_length=200,default='SOME STRING')

class ShowNewsList(models.Model):
    theme = models.CharField(max_length=200)
    text = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    day = models.CharField(max_length=50)
    monthday = models.CharField(max_length=50)
    keywords = models.CharField(max_length=200)
    weblinks = models.CharField(max_length=200,default='SOME STRING')


class KeyWordsList(models.Model):
    keyword = models.CharField(max_length=200)
    weight = models.IntegerField(default=0)

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
class Article(models.Model):
    link = models.CharField(max_length=200)
    keywords = models.TextField()

class Relationship(models.Model):
    id1 = models.IntegerField(default=0)
    id2 = models.IntegerField(default=0)
    score = models.IntegerField(default=0)

class NameForm(forms.Form):
    LinkName = forms.CharField(label='Add Links', max_length=200)
    def __init__(self, *args, **kwargs):
         super(NameForm, self).__init__(*args, **kwargs) # Call to ModelForm constructor
         self.fields['LinkName'].widget.attrs['cols'] = 10
         self.fields['LinkName'].widget.attrs['rows'] = 20
         
class UserInfo(models.Model):
    Username = models.CharField(max_length=100,default=1)
    TravelWeight = models.FloatField(default=1)
    MusicWeight = models.FloatField(default=1)
    PoliticWeight = models.FloatField(default=1)
    EntertainmentWeight = models.FloatField(default=1)
    TechnologyWeight = models.FloatField(default=1)
    # keyword = models.CharField(max_length=200)
    # weight = models.IntegerField(default=0)