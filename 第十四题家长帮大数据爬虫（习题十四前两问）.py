# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 10:02:31 2018
K12（小学到高中12年的简称）--
高考--高考派(统计全中国大学招生情况，例如北京大学(3000)在北京招多少人？在重庆？在全国？)
全中国有多少所大学？
全中国有多少个城市？
在某个城市文科招的人数？理科招生的人数？
====
全国大学招生人数排行：例如
郑州大学 8000
桂林大学 6000
.....
西藏藏医学院：5
=
家长帮班级项目：
注意点：同一时间，访问量过大，可能会导致本次项目无法进行，因为北京那边服务器奔溃。导致全国都无法访问。
导致对方程序员加班。所以我们整个班级，需要有一套策略，要拿到所有数据但不会导致奔溃。
策略例如：
======
题目十四：家长帮大数据爬虫项目
1.根据all_school.txt获取全中国学校网址编号：1304，生成一个2300列表
2.根据http://www.gaokaopai.com/daxue-zhaosheng-学校编号.html 获取全国城市的编号 例如北京：11
3.班级团队(需要下载142600(2300*31*2)次)：
    中国划分区域-分组(城市)
    区域分组员
    如何下载策略-分时间下载
    执行人物2300-分配到自己的任务一般是2300
    保存数据---组长全部合并--班长统计
4.待定

@author: Administrator
"""
import urllib.request as r
url='http://www.gaokaopai.com/daxue-zhaosheng-{}.html'
data='id=2948&type=2&city=50&state=1'.encode()
req=r.Request(url,data=data,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
d=r.urlopen(req).read().decode('utf-8','ignore')
import json
data=json.loads(data)

#############################################################################第一问：找编号
import re
f=open('C:/Users/Administrator/Desktop/18all_school.txt','r',encoding='utf-8')#ctrl+i
a=f.readlines()
s=str(a)
ls=re.compile('jianjie-(.*?).html').findall(s)
for i in range(2300):
    print('编号：{}\n'.format(ls[i]))
##########################################################找编号+学校

####################方法一 找城市、学校、学校编号
import re
f=open('C:/Users/Administrator/Desktop/18all_school.txt','r',encoding='utf-8')#ctrl+i
a=f.readlines()#将所有的文本中的每行读取到一个列表中去   
for i in range(2300):
    k=a[i].split("\t")
    p=re.compile("\d+").findall(k[2])
    print('{}\t{}\t{}'.format(k[0],k[1],p[0]))
    
####################方法二 普通的办法（找学校）
import re
f=open('C:/Users/Administrator/Desktop/18all_school.txt','r',encoding='utf-8')#ctrl+i
a=f.read()#将所有文本读取到一个字符串当中去
ls1=re.compile('jianjie-(.*?).html').findall(a)
ls2=re.compile('(.*?)\t.*\t').findall(a)
for i in range(2300):
    print('学校：{}\t编号：{}\n'.format(ls2[i],ls1[i]))
    
##############################################################################第二题：城市编号
import urllib.request as r
import re
url='http://www.gaokaopai.com/daxue-zhaosheng-477.html'
data='id=2948&type=2&city=50&state=1'.encode()
req=r.Request(url,data=data,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
d=r.urlopen(req).read().decode('utf-8','ignore')

pat1=".setVar\S'claimCity', (.*?)\S\S>"
ls1=re.compile(pat1,re.S).findall(d)
pat2='<li data-val=(.*?) data-id="2"'
ls2=re.compile('<li data-val=(.*?) data-id="2"').findall(d)#不跨行
for j in range(31):
    print('省市：{}   编码：{}'.format(ls2[j].replace('"',''),ls1[j]))

######################################################################














