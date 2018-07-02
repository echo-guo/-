# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 10:43:09 2018


题目十三：糗事百科数据爬取
1.爬取作者和内容
2.爬取13页
3.下载图片。想做就做
@author: Administrator
"""
import urllib.request as r#导入URL工具包 并且命令为r
myconn=r.urlopen('http://www.baidu.com')
if myconn.getcode()==200:
    data=myconn.read().decode('utf-8')
    print(data)
else:
    print('无法访问此网站')
myconn.close()

"""
raise RemoteDisconnected("Remote end closed connection without"
RemoteDisconnected: Remote end closed connection without response
爬虫里面非常关键的：反爬虫
1.直接屏蔽程序爬取数据
2.如果访问对方服务器次数过大，对方会屏蔽你的IP/屏蔽十分钟....

"""
req=r.Request('https://www.qiushibaike.com/',headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'})
myurl=r.urlopen(req)
print(myurl.getcode())
data=myurl.read().decode('utf-8')

pat='<div class="content">(.*?)</div>'
import re
ls=re.compile(pat,re.S).findall(data)

url='https://pic.qiushibaike.com/system/pictures/11292/112920206/medium/app112920206.jpg'
r.urlretrieve(url,'./tmp.jpg')#retrieve下载文件
##############################################################################爬取十三页
import urllib.request as r
import re
for i in range(13):
    req=r.Request('http://www.qiushibaike.com/8hr/page/{}/ '.format(i),headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'})
    myurl=r.urlopen(req)
    data=myurl.read().decode('utf-8')
    ls=re.compile('alt="(.*?)"').findall(data)
    ls1=re.compile('<div class="content">(.*?)</div>',re.S).findall(data)
    for j in range(len(ls1)):
        print('作者为{},\n内容为{}'.format(ls[j],ls1[j]).replace('<span>','').replace('</span>',''))

##########################################################################爬取一页
import urllib.request as r
req=r.Request('https://www.qiushibaike.com/8hr/page/2/',headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'})
myurl=r.urlopen(req)
print(myurl.getcode())
data=myurl.read().decode('utf-8')
import re
print(data)
pat='<div class="content">\n<span>\n\n\n(.*?)\n\n</span>'
ls1=re.compile(pat,re.S).findall(data)
