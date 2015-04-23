#!/usr/bin/python
# -*- coding: utf-8 -*-

# import sqlite3 as lite

#./manage.py shell < articile_into_database.py

import sys
import alchemyapi
# from blog.keyword_handler import KeywordHandler
from blog.models import NewsList

inst = alchemyapi.AlchemyAPI()

###
NewsList.objects.all().delete()

f=open('cnn_news.txt','r')
temp = f.read().splitlines()
num=0
while (num<1):
    url = temp[num]
    num = num +1
    print url
    # url = "http://cnn.com/2015/04/06/opinions/wang-china-women-detained/index.html"
    # url = 'http://edition.cnn.com/2015/04/18/africa/south-africa-xenophobia-explainer/index.html'
    keywords = inst.keywords("url", url)
    text = inst.text("url",url)
    title = inst.title("url",url)
    author = inst.author("url",url)
    print keywords
    if keywords['status'] == 'ERROR':
        continue
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
    print res
    item=NewsList(theme=title,text=text,author=author,weblinks=url,keywords=res)
    item.save()

