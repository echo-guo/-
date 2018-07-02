# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 10:35:57 2018

函数：
变量(生命周期)
全局变量，局部变量(函数内)
练习五:实现练习四，
1.使用函数写出来。定义函数，输出每一天6:00,12:00,18:00的天气信息
2.打印折线图,使用字符串的*号操作
10----------
5-----

@author: Administrator
"""
import urllib.request as r#导入联网工具包，命令为r
url='http://api.openweathermap.org/data/2.5/forecast?q=zhengzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)

#
#time1=data['list'][0]['dt_txt']
#time2=data['list'][2]['dt_txt']
#time3=data['list'][4]['dt_txt']
#time4=data['list'][8]['dt_txt']
#time5=data['list'][10]['dt_txt']
#time6=data['list'][12]['dt_txt']
#time7=data['list'][16]['dt_txt']
#time8=data['list'][18]['dt_txt']
#time9=data['list'][20]['dt_txt']
#time10=data['list'][24]['dt_txt']
#time11=data['list'][26]['dt_txt']
#time12=data['list'][28]['dt_txt']
#time13=data['list'][32]['dt_txt']
#time14=data['list'][34]['dt_txt']
#time15=data['list'][36]['dt_txt']
#
#temp1=data['list'][0]['main']['temp']
#temp2=data['list'][2]['main']['temp']
#temp3=data['list'][4]['main']['temp']
#temp4=data['list'][8]['main']['temp']
#temp5=data['list'][10]['main']['temp']
#temp6=data['list'][12]['main']['temp']
#temp7=data['list'][16]['main']['temp']
#temp8=data['list'][18]['main']['temp']
#temp9=data['list'][20]['main']['temp']
#temp10=data['list'][24]['main']['temp']
#temp11=data['list'][26]['main']['temp']
#temp12=data['list'][28]['main']['temp']
#temp13=data['list'][32]['main']['temp']
#temp14=data['list'][34]['main']['temp']
#temp15=data['list'][36]['main']['temp']
#
#description1=data['list'][0]['weather'][0]['main']
#description2=data['list'][2]['weather'][0]['main']
#description3=data['list'][4]['weather'][0]['main']
#description4=data['list'][8]['weather'][0]['main']
#description5=data['list'][10]['weather'][0]['main']
#description6=data['list'][12]['weather'][0]['main']
#description7=data['list'][16]['weather'][0]['main']
#description8=data['list'][18]['weather'][0]['main']
#description9=data['list'][20]['weather'][0]['main']
#description10=data['list'][24]['weather'][0]['main']
#description11=data['list'][26]['weather'][0]['main']
#description12=data['list'][28]['weather'][0]['main']
#description13=data['list'][32]['weather'][0]['main']
#description14=data['list'][34]['weather'][0]['main']
#description15=data['list'][36]['weather'][0]['main']
#
#temp1=str(temp1)

def msg(time,temp,des,pre,temp_max,temp_min):
    print('当时间为：{}时'.format(time))
    print('温度是：{}'.format(temp))
    print('今天天气是：{}'.format(des))
    print('今天气压是：{}'.format(pre))
    print('今天最高温度是：{}'.format(temp_max))
    print('今天最低温度是：{}'.format(temp_min))
a=0
    

def msg(t):
    a=data['city']['name']
    b=data['list'][t]['dt_txt']
    c=data['list'][t]['weather'][0]['main']
    d=data['list'][t]['main']['pressure']
    e=data['list'][t]['main']['temp_max']
    f=data['list'][t]['main']['temp_min']
    g=data['list'][t]['main']['temp']
    print('{}{}时,天气为：{},气压为：{},最高温为：{},最低温为：{},当天温度为：{}'.format(a,b,c,d,e,f,g))
    msg(0)
    msg(2)
    msg(4)
    msg(8)
    msg(10)
    msg(12)
    msg(16)
    msg(18)
    msg(20)
    msg(24)
    msg(26)
    msg(28)
    msg(32)
    msg(34)
    msg(36)

def msg(y):
    b=data['list'][y]['dt_txt']
    g=data['list'][y]['main']['temp']
    h=int(g)*'*'
    print('时间是：{},温度是：{},折线图是：{}'.format(b,g,h))
    
    msg(0)
    msg(2)
    msg(4)
    msg(8)
    msg(10)
    msg(12)
    msg(16)
    msg(18)
    msg(20)
    msg(24)
    msg(26)
    msg(28)
    msg(32)
    msg(34)
    msg(36)
