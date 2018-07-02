# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 10:56:03 2018

@author: Administrator
"""

import urllib.request as r#导入联网工具包，命令为r
url='http://api.openweathermap.org/data/2.5/forecast?q=zhengzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)
#data字典-》list列表-》index 0 字典-》main字典-》temp变量
city=data['city']['name']
time=data['list'][i]['dt_txt']
des=data['list'][i]['weather'][0]['main']
print('{}  时间为：{}  天气为：{}'.format(city,time,des))
#########################
#三天天气
for i in range(5,30,3):
    city=data['city']['name']
    time=data['list'][i]['dt_txt'] 
    des=data['list'][i]['weather'][0]['description']
    if des=='晴，少云':
        print('{}  时间为：{}  天气为：{}  建议：出去游玩'.format(city,time,des))
    elif des=='晴':
        print('{}  时间为：{}  天气为：{}  建议：出去游玩，减少衣服，注意防晒'.format(city,time,des))
    elif des=='多云':
        print('{}  时间为：{}  天气为：{}  建议：增加衣物，出门带伞'.format(city,time,des))
    else:
        print('{}  时间为：{}  天气为：{}  建议：增加衣物，出门带伞'.format(city,time,des))

##########################
#雪花闪屏

for i in range(0,23):
    if i==0:
        print(' '*12, '     ＊   ' *2,' '*12)
    elif i%2==1:
        print('')
    elif i==2:
        print(' '*19, '        ＊       ' *3,' '*7)
    elif i==4:
        print('')
    elif i==6:
        print(' '*13, '     ＊     ' *7,' '*7)
    elif i==8:
        print('')
    elif i==10:
        print(' '*10, '      ＊     ' *3,' '*12)
    elif i==12:
        print(' '*11, '      ＊     ' *5,' '*11)
    elif i==14:
        print(' '*10, '       ＊      ' *7,' '*10)
    elif i==16:
        print(' '*9, '        ＊       ' *10,' '*9)
    elif i==18:
        print(' '*7, '           ＊            ' *9,' '*5)
    elif i==20:
        print(' '*5, '       ＊         ' *9,' '*8)
    elif i==22:
        print(' '*40,'欢 迎 收 看 天 气 预 报',' '*20)
