# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 09:50:57 2018

@author: Administrator
"""
import turtle
t = turtle.Pen()
turtle.bgcolor("black")
sides=7
colors=["steelblue","lightskyblue","skyblue","deepskyblue","lightblue",'powderblue','aqua']
for x in range(70):
    t.pencolor(colors[x%sides])
    t.forward(x*25/sides+x)
    t.left(360/sides+1)
    t.width(x*sides/200)

s=[]
ls=[]
ls1=[]
ls2=[]
ls3=[]
import re
import urllib.request as r
for i in range(1,7):
    url='http://dianying.2345.com/list/jingdian-------{}.html'.format(i)
    req=r.Request(url,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'})
    p=r.urlopen(req).read().decode('gbk','ignore')
    pat='<a title="(.*?)" target'
    pat1='target="_blank" href="//dianying.2345.com/detail/(.*?).html'
    ls=re.compile(pat,re.S).findall(p)
    ls2=re.compile(pat1,re.S).findall(p)
    for j in range(len(ls)):
        ls1.append(ls[j])
        ls3.append(ls2[j])
for ln in range(len(ls1)):
    print('{}:电影:{}'.format(ln,ls1[ln]))
for k in range(len(ls3)):
    url='http://dianying.2345.com/detail/{}.html '.format(ls3[k])
    req=r.Request(url,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'})
    data=r.urlopen(url).read().decode('gbk')
    s.append(data)
p=open('./jingdian3.txt','w')
import re
for i in range(len(s)):
    a=re.compile('<h1>(.*?)</h1>',re.S).findall(s[i])
    b=re.compile('<span class="sAll">(.*?)</span>',re.S).findall(s[i])
    p.write('{}--电影名:{}  简介:{}\n'.format(i,a,b).replace("['",'').replace("']",'').replace("']",'').replace("'\r\n'",'').replace('\u3000\u3000',''))
p.close()                  
f=open('./jingdian3.txt','r')
ls4=f.readlines() 
ls4=open('./jingdian3.txt','r').readlines()
def xuhao(s):
    abc=''
    for i in ls4:
        if s==i.split('--')[0]:
            abc=i.split('--')[1]
            break
    return abc
while True:    
    shuzi=input("（备注：输入大于204号则退出APP）\n 以下APP为您推荐的人生必看百部电影，请您输入您感兴趣电影的序号: ") 
    x=xuhao(shuzi)
    print(x)
    if int(shuzi)>204: 
        break


        
    
        
        
    