# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 10:30:48 2018

字典dict：
{str:type,...}
第二题：
1.定义一个字典：里面存储7天的天气信息，信息有：7天的温度，7天的天气情况，今天最高温度
2.打印星期三的温度和天气情况，以及打印今天的最高温度

@author: Administrator
"""
msg={'a':['rain','sun','rain','sun','rain','sun','rain'],
     'b':['25','24','27','28','29','36','31'],
     'c':34}
print("星期三的温度是:"+str(msg['a'][2]) ,"星期三的天气是"+str(msg['b'][2]),"星期三的最高温度是"+str(msg['c']))
