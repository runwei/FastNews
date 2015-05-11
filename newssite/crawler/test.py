import json
import sys
from userInfo import userInfo 
# from pprint import pprint

num=0
with open('data_utf8.json') as fp:
    for line in fp:
        data=json.loads(line)
        if data.has_key('keywords') :
            # print data['keywords']
            # if data['keywords'][0] == u'world':
            #     usr = userInfo("world")
            #     url = data['link'][0]
            #     print url
            #     usr.set_bookmark(url)
            if data['keywords'][0] == u'sport':
                usr = userInfo("sport")   
                url = data['link'][0]
                print url
                usr.set_bookmark(url)        
                # print data['title'][0]
                
            
        # print data['desc']

