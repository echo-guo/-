# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 14:03:11 2018

@author: Administrator
"""

import urllib.request as r
url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With': 'XMLHttpRequest'}
req=r.Request(url,headers=headers,data='id=477&type=2&city=23&state=1'.encode())
data=r.urlopen(req).read().decode('utf-8','ignore')

#东北
#黑龙江	吉林 	辽宁
area={'黑龙江':'东北','吉林':'东北','辽宁':'东北'}
areaplan={'东北':0}
areaplan['东北']=areaplan['东北']+8
###########通过下面定义多个变量赋值，计算出中国地区的人数
a=0
b=0
c=0
if '东北'==plan:
   a=a+1 

import json
data=json.loads(data)

for i in range(142600):
    if data['status']==1:
        ls=data['data']
    for school in ls:
        city=school['city']
        print(area[city])
        print(int(school['plan']))
        areaplan[area[city]]=areaplan[area[city]]+int(school['plan'])
##############################################################################
#d='id=477&type=2&city=23&state=1'.encode()#bytes
#print(d)
#print(type(d))
    #ls1[i]=int(ls1[i])

#############################################计算海南理科招生人数代码（字符串---正则得到人数）
import re
f=open('C:/Users/Administrator/Desktop/18第三问（成品）.txt','r',encoding='utf-8')#ctrl+i
g=f.read()    
#import json
#data=json.loads(a)
ls1=re.compile('"plan":"(.*?)","uniname"').findall(g)
sum=0
for i in range(len(ls1)):
    ls1[i]=int(ls1[i])
    sum+=ls1[i]
    a=sum
print('海南理科人数：{}\n'.format(a))
###########################################计算海南理科招生人数代码（以行读入列表---转换为字典）
sum=0
b={}
ls=[]
f=open('C:/Users/Administrator/Desktop/广东理科.txt')
a=f.readlines()#将文本中的每行数据读入列表
import json
for i in range(2300):
    b[i]=json.loads(a[i])
for q in range(2300):
    if b[q]['status']==1:
        ls.append(b[q])
for m in range(1074):
    for k in range(len(ls[m]['data'])):
        d=ls[m]['data'][k]['plan']
        sum+=int(d)
print('在广东理科招生人数为：{}'.format(sum))

################（正则）海南理科a 海南文科b 广东理科c 广东文科d 广西理科e 广西文科f （文件名与字母随意切换）
import re
f=open('C:/Users/Administrator/Desktop/广西文科.txt','r',encoding='utf-8')#ctrl+i
g=f.read()    
#import json
#data=json.loads(a)
ls1=re.compile('"plan":"(.*?)","uniname"').findall(g)
sum=0
for i in range(len(ls1)):
    ls1[i]=int(ls1[i])
    sum+=ls1[i]
    f=sum
print('海南理科人数：{}\n'.format(f))

##################################################### 计算华南地区总人数
ls=[a,b,c,d,e,f]
h=0
for i in range(len(ls)):
    h+=ls[i]
print('在华南地区招生总人数为：{}'.format(h))

########################################################






