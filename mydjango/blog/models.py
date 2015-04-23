from django.db import models
from django import forms
# from django.forms.util import ErrorList
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
# import datetime


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

class AddLinkForm(forms.Form):
    LinkName = forms.CharField(label='Add Links', max_length=200)
    def __init__(self, *args, **kwargs):
         super(AddLinkForm, self).__init__(*args, **kwargs) # Call to ModelForm constructor
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