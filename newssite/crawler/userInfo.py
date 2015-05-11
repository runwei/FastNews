import sys
import hashlib
from article2db import article2db 
from boto.s3.key import Key
from boto.s3.connection import S3Connection

class userInfo:    
    def __init__(self,username):
        s3 = S3Connection('AKIAILFPCHJZ4B4S6WBA','14dMH/aJM9a0X+nAC2FYufcVhnm/fQxc5AWvaxnp')
        self.bucket=s3.get_bucket('userinfo') 
        self.art = article2db()
        self.username = username
        
    def set_bookmark(self,url):
        if not self.art.exist_url(url):
            if not self.art.put_url(url):
                return False
        hashnum = hashlib.md5(url).hexdigest()
        possiblekey = self.bucket.get_key(hashnum+"_"+self.username+"_bkm")
        if (possiblekey) is None:
            self.store_key_value(hashnum+"_"+self.username+"_bkm", "1")
        return True

        
        
    def get_bookmarks(self):
        keylist = [] 
        resultlist = []
        for key in self.bucket.list():
            [hashnum,username,flag]=key.name.split("_")
            if username == self.username and flag=="bkm":
                # print username
                # keylist.append(hashnum)
                if  self.art.exist_hashnum(hashnum):
                    result =self.art.retrieve_news(hashnum)
                    resultlist.append(result)
        return resultlist

    def get_bookmark_scroll(self,number,offset):
        keylist = [] 
        resultlist = []
        for key in self.bucket.list():
            [hashnum,username,flag]=key.name.split("_")
            if username == self.username and flag=="bkm":
                # print username
                # keylist.append(hashnum)
                if  self.art.exist_hashnum(hashnum):
                    result =self.art.retrieve_news(hashnum)
                    resultlist.append(result)
        return resultlist[offset:offset+number]

    def set_recommendations(self,url):
        if not self.art.exist_url(url):
            if not self.art.put_url(url):
                return False
        hashnum = hashlib.md5(url).hexdigest()
        possiblekey = self.bucket.get_key(hashnum+"_"+self.username+"_rcm")
        if (possiblekey) is None:
            self.store_key_value(hashnum+"_"+self.username+"_rcm", "1")
        return True

        
        
    def get_recommendations(self):
        keylist = [] 
        resultlist = []
        for key in self.bucket.list():
            [hashnum,username,flag]=key.name.split("_")
            if username == self.username and flag=="rcm":
                # print username
                # keylist.append(hashnum)
                if  self.art.exist_hashnum(hashnum):
                    result =self.art.retrieve_news(hashnum)
                    resultlist.append(result)
        return resultlist    
        
        
    def store_key_value(self,key,value):
        possiblekey = self.bucket.get_key(key)
        if possiblekey is None:
            k = Key(self.bucket)
            k.key = key
            k.set_contents_from_string(value)
            return True
        else:
            return False

def store_url_test():
    # parse command line options
    usr = userInfo("anonymous")
    f=open('cnn_news.txt','r')
    temp = f.read().splitlines()
    num = 0
    while (num<20):
        # url = "http://cnn.com/2015/04/12/football/manchester-united-city-chelsea-football/index.html"
        url = temp[num]
        num = num +1
        print url
        usr.set_bookmark(url)

def retrieve_test():
    usr = userInfo("anonymous")   
    resultlist = usr.get_bookmarks()
    for result in resultlist:
        print result['title']
    
def main():
    store_url_test()
        


if __name__ == "__main__":
    main()
