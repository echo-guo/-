# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 10:50:20 2018

@author: Administrator
"""

#####################################################习题十二  天气预报

import urllib.request as r#导入联网工具包，命令为r  python
url='http://api.openweathermap.org/data/2.5/forecast?q=zhengzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
print(data)
import re
ls1=re.compile('"dt_txt":"(.*?)"}').findall(data)
ls2=re.compile('"description":"(.*?)","icon').findall(data)
ls3=re.compile('":{"temp":(.*?),"temp_min').findall(data)
ls4=re.compile('"pressure":(.*?),"sea_level').findall(data)
for i in range(len(ls1)):
    print('郑州 {}  天气：{}   温度：{}  气压：{}'.format(ls1[i],ls2[i],ls3[i],ls4[i]))