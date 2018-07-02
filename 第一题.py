# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 10:29:56 2018
Spyder Editor
ctrl +   方法字体
ctrl enter  选中运行
第一题
1.定义一个天气列表。写出里面一周每个温度
2.打印出7天的天气，并且如果是星期三的话，打印星期三是X度
@author: Administrator
"""



temprature=[15,11,12,13,16,18,25]
print(temprature[0])
print(temprature[1])
print("星期三是:"+str(temprature[2]))
print(temprature[3])
print(temprature[4])
print(temprature[5])
print(temprature[6])




msg={'a':['rain','sun','rain','sun','rain','sun','rain'],
     'b':['25','24','27','28','29','36','31'],
     'c':['34']}
msg['a'][2]
msg['b'][2]
msg['c'][2]
print("星期三的温度是:"+str(msg['a'][2]) ,"星期三的天气是"+str(msg['b'][2]),"星期三的最高温度是"+str(msg['c'][0]))