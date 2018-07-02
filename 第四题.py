# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 10:33:30 2018

全球未来5天气预报
2018-06-21 03:00:00    按照3小时一次预报
2018-06-21 06:00:00
2018-06-21 09:00:00------当前时间
2018-06-21 12:00:00
2018-06-25 21:00:00

第四题：求出未来5天天气
1.打印每天的6:00,12:00,18:00的天气(城市,温度，情况，气压，最高温度，最低温度)
2.同上写出[英文版的]
3.根据天气的情况，给出建议：例如，今天下雨，提示带伞。今天温度高，穿衬衫...三个件以上
4.根据温度打印出问题折线图
    28——————————————————————————————
    30——————————————————————————————————
    10——————————————————
5.打印出其他10个城市的天气，计算出天气排名，按着大到小的顺序。

@author: Administrator
"""
import urllib.request as r#导入联网工具包，命令为r
url='http://api.openweathermap.org/data/2.5/forecast?q=zhengzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)
#data字典-》list列表-》index 0 字典-》main字典-》temp变量
city1=data['city']['name']

time1=data['list'][0]['dt_txt']
time2=data['list'][2]['dt_txt']
time3=data['list'][4]['dt_txt']
time4=data['list'][8]['dt_txt']
time5=data['list'][10]['dt_txt']
time6=data['list'][12]['dt_txt']
time7=data['list'][16]['dt_txt']
time8=data['list'][18]['dt_txt']
time9=data['list'][20]['dt_txt']
time10=data['list'][24]['dt_txt']
time11=data['list'][26]['dt_txt']
time12=data['list'][28]['dt_txt']
time13=data['list'][32]['dt_txt']
time14=data['list'][34]['dt_txt']
time15=data['list'][36]['dt_txt']

temp1=data['list'][0]['main']['temp']
temp2=data['list'][2]['main']['temp']
temp3=data['list'][4]['main']['temp']
temp4=data['list'][8]['main']['temp']
temp5=data['list'][10]['main']['temp']
temp6=data['list'][12]['main']['temp']
temp7=data['list'][16]['main']['temp']
temp8=data['list'][18]['main']['temp']
temp9=data['list'][20]['main']['temp']
temp10=data['list'][24]['main']['temp']
temp11=data['list'][26]['main']['temp']
temp12=data['list'][28]['main']['temp']
temp13=data['list'][32]['main']['temp']
temp14=data['list'][34]['main']['temp']
temp15=data['list'][36]['main']['temp']

description1=data['list'][0]['weather'][0]['main']
description2=data['list'][2]['weather'][0]['main']
description3=data['list'][4]['weather'][0]['main']
description4=data['list'][8]['weather'][0]['main']
description5=data['list'][10]['weather'][0]['main']
description6=data['list'][12]['weather'][0]['main']
description7=data['list'][16]['weather'][0]['main']
description8=data['list'][18]['weather'][0]['main']
description9=data['list'][20]['weather'][0]['main']
description10=data['list'][24]['weather'][0]['main']
description11=data['list'][26]['weather'][0]['main']
description12=data['list'][28]['weather'][0]['main']
description13=data['list'][32]['weather'][0]['main']
description14=data['list'][34]['weather'][0]['main']
description15=data['list'][36]['weather'][0]['main']

pre1=data['list'][0]['main']['pressure']
pre2=data['list'][2]['main']['pressure']
pre3=data['list'][4]['main']['pressure']
pre4=data['list'][8]['main']['pressure']
pre5=data['list'][10]['main']['pressure']
pre6=data['list'][12]['main']['pressure']
pre7=data['list'][16]['main']['pressure']
pre8=data['list'][18]['main']['pressure']
pre9=data['list'][20]['main']['pressure']
pre10=data['list'][24]['main']['pressure']
pre11=data['list'][26]['main']['pressure']
pre12=data['list'][28]['main']['pressure']
pre13=data['list'][32]['main']['pressure']
pre14=data['list'][34]['main']['pressure']
pre15=data['list'][36]['main']['pressure']


temp_max1=data['list'][0]['main']['temp_max']
temp_max2=data['list'][2]['main']['temp_max']
temp_max3=data['list'][4]['main']['temp_max']
temp_max4=data['list'][8]['main']['temp_max']
temp_max5=data['list'][10]['main']['temp_max']
temp_max6=data['list'][12]['main']['temp_max']
temp_max7=data['list'][16]['main']['temp_max']
temp_max8=data['list'][18]['main']['temp_max']
temp_max9=data['list'][20]['main']['temp_max']
temp_max10=data['list'][24]['main']['temp_max']
temp_max11=data['list'][26]['main']['temp_max']
temp_max12=data['list'][28]['main']['temp_max']
temp_max13=data['list'][32]['main']['temp_max']
temp_max14=data['list'][34]['main']['temp_max']
temp_max15=data['list'][36]['main']['temp_max']


temp_min1=data['list'][0]['main']['temp_min']
temp_min2=data['list'][2]['main']['temp_min']
temp_min3=data['list'][4]['main']['temp_min']
temp_min4=data['list'][8]['main']['temp_min']
temp_min5=data['list'][10]['main']['temp_min']
temp_min6=data['list'][12]['main']['temp_min']
temp_min7=data['list'][16]['main']['temp_min']
temp_min8=data['list'][18]['main']['temp_min']
temp_min9=data['list'][20]['main']['temp_min']
temp_min10=data['list'][24]['main']['temp_min']
temp_min11=data['list'][26]['main']['temp_min']
temp_min12=data['list'][28]['main']['temp_min']
temp_min13=data['list'][32]['main']['temp_min']
temp_min14=data['list'][34]['main']['temp_min']
temp_min15=data['list'][36]['main']['temp_min']


data['list'][0]['main']['temp']
#data字典-》list列表-》index 0 字典-》main字典-》temp_max变量

#data字典-》list列表-》index 0 字典-》main字典-》temp_min变量

##################################################英文
s=print('{}{} temprature is：{},pressure is：{}，the highest temprature is：{}，the lowest temprature is：{},the description is:{},建议：游玩'.format(city1,time1,temp1,pre1,temp_max1,temp_min1,description1),
        '{}{} temprature is：{},pressure is：{}，the highest temprature is：{}，the lowest temprature is：{},the description is:{},建议：游玩'.format(city1,time2,temp2,pre2,temp_max2,temp_min2,description2),
        '{}{} temprature is：{},pressure is：{}，the highest temprature is：{}，the lowest temprature is：{},the description is:{},建议：游玩'.format(city1,time3,temp3,pre3,temp_max3,temp_min3,description3),
        '{}{} temprature is：{},pressure is：{}，the highest temprature is：{}，the lowest temprature is：{},the description is:{},建议：游玩'.format(city1,time4,temp4,pre4,temp_max4,temp_min4,description4),
        '{}{} temprature is：{},pressure is：{}，the highest temprature is：{}，the lowest temprature is：{},the description is:{},建议：游玩'.format(city1,time5,temp5,pre5,temp_max5,temp_min5,description5),
        '{}{} temprature is：{},pressure is：{}，the highest temprature is：{}，the lowest temprature is：{},the description is:{},建议：游玩'.format(city1,time6,temp6,pre6,temp_max6,temp_min6,description6),
        '{}{} temprature is：{},pressure is：{}，the highest temprature is：{}，the lowest temprature is：{},the description is:{},建议：游玩'.format(city1,time7,temp7,pre7,temp_max7,temp_min7,description7),
        '{}{} temprature is：{},pressure is：{}，the highest temprature is：{}，the lowest temprature is：{},the description is:{},建议：游玩'.format(city1,time8,temp8,pre8,temp_max8,temp_min8,description8),
        '{}{} temprature is：{},pressure is：{}，the highest temprature is：{}，the lowest temprature is：{},the description is:{},建议：游玩'.format(city1,time9,temp9,pre9,temp_max9,temp_min9,description9),
        '{}{} temprature is：{},pressure is：{}，the highest temprature is：{}，the lowest temprature is：{},the description is:{},建议：游玩'.format(city1,time10,temp10,pre10,temp_max10,temp_min10,description10),
        '{}{} temprature is：{},pressure is：{}，the highest temprature is：{}，the lowest temprature is：{},the description is:{},建议：游玩'.format(city1,time11,temp11,pre11,temp_max11,temp_min11,description11),
        '{}{} temprature is：{},pressure is：{}，the highest temprature is：{}，the lowest temprature is：{},the description is:{},建议：游玩'.format(city1,time12,temp12,pre12,temp_max12,temp_min12,description12),
        '{}{} temprature is：{},pressure is：{}，the highest temprature is：{}，the lowest temprature is：{},the description is:{},建议：游玩'.format(city1,time13,temp13,pre13,temp_max13,temp_min13,description13),
        '{}{} temprature is：{},pressure is：{}，the highest temprature is：{}，the lowest temprature is：{},the description is:{},建议：游玩'.format(city1,time14,temp14,pre14,temp_max14,temp_min14,description14),
        '{}{} temprature is：{},pressure is：{}，the highest temprature is：{}，the lowest temprature is：{},the description is:{},建议：出门带伞'.format(city1,time15,temp15,pre15,temp_max15,temp_min15,description15))

##############################################中文
s=print('{}{}的温度为：{},气压为：{}，最高温度为：{}，最低温度为：{},天气情况为：{},建议：游玩'.format(city1,time1,temp1,pre1,temp_max1,temp_min1,description1),
        '{}{}的温度为：{},气压为：{}，最高温度为：{}，最低温度为：{},天气情况为：{},建议：游玩'.format(city1,time2,temp2,pre2,temp_max2,temp_min2,description2),
        '{}{}的温度为：{},气压为：{}，最高温度为：{}，最低温度为：{},天气情况为：{},建议：游玩'.format(city1,time3,temp3,pre3,temp_max3,temp_min3,description3),
        '{}{}的温度为：{},气压为：{}，最高温度为：{}，最低温度为：{},天气情况为：{},建议：游玩'.format(city1,time4,temp4,pre4,temp_max4,temp_min4,description4),
        '{}{}的温度为：{},气压为：{}，最高温度为：{}，最低温度为：{},天气情况为：{},建议：游玩'.format(city1,time5,temp5,pre5,temp_max5,temp_min5,description5),
        '{}{}的温度为：{},气压为：{}，最高温度为：{}，最低温度为：{},天气情况为：{},建议：游玩'.format(city1,time6,temp6,pre6,temp_max6,temp_min6,description6),
        '{}{}的温度为：{},气压为：{}，最高温度为：{}，最低温度为：{},天气情况为：{},建议：游玩'.format(city1,time7,temp7,pre7,temp_max7,temp_min7,description7),
        '{}{}的温度为：{},气压为：{}，最高温度为：{}，最低温度为：{},天气情况为：{},建议：游玩'.format(city1,time8,temp8,pre8,temp_max8,temp_min8,description8),
        '{}{}的温度为：{},气压为：{}，最高温度为：{}，最低温度为：{},天气情况为：{},建议：游玩'.format(city1,time9,temp9,pre9,temp_max9,temp_min9,description9),
        '{}{}的温度为：{},气压为：{}，最高温度为：{}，最低温度为：{},天气情况为：{},建议：游玩'.format(city1,time10,temp10,pre10,temp_max10,temp_min10,description10),
        '{}{}的温度为：{},气压为：{}，最高温度为：{}，最低温度为：{},天气情况为：{},建议：游玩'.format(city1,time11,temp11,pre11,temp_max11,temp_min11,description11),
        '{}{}的温度为：{},气压为：{}，最高温度为：{}，最低温度为：{},天气情况为：{},建议：游玩'.format(city1,time12,temp12,pre12,temp_max12,temp_min12,description12),
        '{}{}的温度为：{},气压为：{}，最高温度为：{}，最低温度为：{},天气情况为：{},建议：游玩'.format(city1,time13,temp13,pre13,temp_max13,temp_min13,description13),
        '{}{}的温度为：{},气压为：{}，最高温度为：{}，最低温度为：{},天气情况为：{},建议：游玩'.format(city1,time14,temp14,pre14,temp_max14,temp_min14,description14),
        '{}{}的温度为：{},气压为：{}，最高温度为：{}，最低温度为：{},天气情况为：{},建议：出门带伞'.format(city1,time15,temp15,pre15,temp_max15,temp_min15,description15))


#description1=data['list'][0]['weather'][0]['description']
#description2=data['list'][2]['weather'][0]['description']
#description3=data['list'][4]['weather'][0]['description']
#description4=data['list'][8]['weather'][0]['description']
#description5=data['list'][10]['weather'][0]['description']
#description6=data['list'][12]['weather'][0]['description']
#description7=data['list'][16]['weather'][0]['description']
#description8=data['list'][18]['weather'][0]['description']
#description9=data['list'][20]['weather'][0]['description']
#description10=data['list'][24]['weather'][0]['description']
#description11=data['list'][26]['weather'][0]['description']
#description12=data['list'][28]['weather'][0]['description']
#description13=data['list'][32]['weather'][0]['description']
#description14=data['list'][34]['weather'][0]['description']
#description15=data['list'][36]['weather'][0]['description']

##############################################打印温度折线图
print(int(temp1)*"-")
print(int(temp2)*"-")
print(int(temp3)*"-")
print(int(temp4)*"-")
print(int(temp5)*"-")
print(int(temp6)*"-")
print(int(temp7)*"-")
print(int(temp8)*"-")
print(int(temp9)*"-")
print(int(temp10)*"-")
print(int(temp11)*"-")
print(int(temp12)*"-")
print(int(temp13)*"-")
print(int(temp14)*"-")
print(int(temp15)*"-")


#############################################第五问 10个城市
import urllib.request as r#导入联网工具包，命令为r
url='http://api.openweathermap.org/data/2.5/forecast?q=zhengzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)
#data字典-》list列表-》index 0 字典-》main字典-》temp变量
#zhengzhou
city1=data['city']['name']
time1=data['list'][0]['dt_txt']

import urllib.request as r#导入联网工具包，命令为r
url='http://api.openweathermap.org/data/2.5/forecast?q=tianjin,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)
#data字典-》list列表-》index 0 字典-》main字典-
#chongqing
city2=data['city']['name']
t2=data['list'][0]['dt_txt']
#shanghai
city3=data['city']['name']
time3=data['list'][0]['dt_txt']
#guangzhou
city4=data['city']['name']
time4=data['list'][0]['dt_txt']
#shenzhen
city5=data['city']['name']
time5=data['list'][0]['dt_txt']
#beijing
city6=data['city']['name']
time6=data['list'][0]['dt_txt']
#nanjing
city7=data['city']['name']
time7=data['list'][0]['dt_txt']
#wuhan
city8=data['city']['name']
time8=data['list'][0]['dt_txt']
#chengdu
city9=data['city']['name']
time9=data['list'][0]['dt_txt']
#tianjin
city10=data['city']['name']
time10=data['list'][0]['dt_txt']
###########################郑州10个时间段的温度排名
ls=[]
ls.append(temp1)
ls.append(temp2)
ls.append(temp3)
ls.append(temp4)
ls.append(temp5)
ls.append(temp6)
ls.append(temp7)
ls.append(temp8)
ls.append(temp9)
ls.append(temp10)
ls=sorted(ls)
ls=reversed(ls)
print(list(ls))
