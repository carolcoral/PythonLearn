'''
Created on 2018年2月9日

@author: Carol

@description: 利用 python 的 urllib 插件扒取网页的图片并下载到本地

1.抓取网页
2.获取图片地址
3.抓取图片内容并保存在本地

'''

#coding:utf8
import urllib
import re

req = urllib.request.urlopen("https://www.imooc.com/course/list")
buf = req.read().encode("utf8")
listurl = re.findall(r'img4.mukewang.com/.+\. jpg',buf)
i =0
for url in listurl:
    f = open(str(i)+'.jpg','w')
    req = urllib.request.urlopen(url)
    buf = req.read()
    f.write(buf)
    i+=1