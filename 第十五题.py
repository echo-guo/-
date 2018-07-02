# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 10:45:13 2018

题目十五：未来三天 天气类天气对象
1.定义一个天气类Weather 静态的属性(temp,description,pre) 动态属性(msg打印当前天气属性)
2.创建3天的天气对象，并调用msg方法

@author: Administrator
"""
########################################################################第一问 定义静态属性
class Forecast:
    def __init__(self,city,time,temp,des,pre):
        self.city=city
        self.time=time
        self.temp=temp
        self.des=des
        self.pre=pre
    def msg(self):
        print("城市：{},时间：{},温度：{},天气情况为：{},气压为：{}".format(self.city,self.time,self.temp,self.des,self.pre))
a=Forecast('郑州','2018-6-29 12:00:00','34.77','多云','995')
print(a.city)
print(a.temp)
print(a.des)
print(a.pre)
a.msg() 

#######################################################################第二问 动态属性（联网 得到未来三天的）
###################三天的天气对象
import urllib.request as r#导入联网工具包，命令为r
url='http://api.openweathermap.org/data/2.5/forecast?q=zhengzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)
class Forecast:
    def __init__(self,city,time,temp,des,pre):
        self.city=city
        self.time=time
        self.temp=temp
        self.des=des
        self.pre=pre
    def msg(self):
        print("城市：{},时间：{},温度：{},天气情况为：{},气压为：{}".format(self.city,self.time,self.temp,self.des,self.pre))
for i in range(0,24,2):
    city=data['city']['name']
    time=data['list'][i]['dt_txt']
    temp=data['list'][i]['main']['temp']
    des=data['list'][i]['weather'][0]['main']
    pre=data['list'][i]['main']['pressure']
    fore=Forecast(city,time,temp,des,pre)
    fore.msg()


