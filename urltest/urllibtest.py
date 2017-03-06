#coding:utf-8

'''
Created on 2016年10月12日

@author: wenxianzhi
'''
from urllib2 import Request
'''
#1 获取网页信息
import urllib
resp=urllib.urlopen('http://www.baidu.com')
print resp
print resp.read().decode('utf-8')
'''

'''
#2 携带user-agent

import urllib2
req = urllib2.Request("http://www.baidu.com")
req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36")
resp = urllib2.urlopen(req)
#resp = urllib.urlopen(req)
print (resp.read().decode("utf-8"))
'''

#post
import urllib
import urllib2
#print dir(urllib)
#print dir(urllib2)







