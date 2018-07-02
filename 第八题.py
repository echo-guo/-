# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 10:40:51 2018

第七题：保存淘宝数据(小组项目)
1.每个组员爬取100页数据(同一种商品)，条件是北京，上海，广州，成都...
2.保存的商品信息有(同第六题),并且是以为csv格式保存
3.单个组员求出当前城市的商品的众数(最多的价格)
4.小组文件合并，求出商品的平均价格

@author: Administrator
"""

import urllib.request as r#导入联网工具包，命令为r
url='https://s.taobao.com/search?q=%E9%9E%8B%E5%AD%90&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&loc=%E9%83%91%E5%B7%9E&ajax=true'
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)

######################################100页数据
f=open('C:/Users/Administrator/Desktop/郭/b.csv','w')
import urllib.request as r#导入联网工具包，命令为r
for i in range(0,100):
    url='https://s.taobao.com/search?q=%E9%9E%8B%E5%AD%90&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&loc=%E9%83%91%E5%B7%9E&bcoffset=6&ntoffset=6&p4ppushleft=1%2C48&s={}&ajax=true'.format(i*44)
    data=r.urlopen(url).read().decode('utf-8')
    import json
    data=json.loads(data)
    for j in range(len(data['mods']['itemlist']['data']['auctions'])):
        a=data['mods']['itemlist']['data']['auctions'][j]['raw_title']
        b=data['mods']['itemlist']['data']['auctions'][j]['view_price']
        c=data['mods']['itemlist']['data']['auctions'][j]['nick']
        d=data['mods']['itemlist']['data']['auctions'][j]['view_sales']
        f.write("{},{},{},{}\n".format(a,b,c,d))
f.close()

############################################################################# 第二问：求众数
#########################求众数的方法一（老师教的）
import csv
with open('C:/Users/Administrator/Desktop/a.csv','r') as csvfile:
    reader=csv.reader(csvfile)
    c=[row[1] for row in reader]
print(c)
c#是一个list
l=set(c)
myls=[]
for i in l:
    myls.append('{}-{}'.format(i,c.count(i)))
mysort=lambda x:int(x.split('-')[1])
myls.sort(key=mysort,reverse=True)#降序，列表中的每个元素都会调用一次mysort函数
zhongshu=myls[0].split('-')
print('出现次数对多的元素是：{} 次数是：{}'.format(zhongshu[0],zhongshu[1]))

######################################################################
#########################求众数方法二(唐)
from scipy.stats import mode
ls=[]
for i in range(0,100):
    url='https://s.taobao.com/search?q=%E9%9E%8B%E5%AD%90&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&loc=%E9%83%91%E5%B7%9E&bcoffset=6&ntoffset=6&p4ppushleft=1%2C48&s={}&ajax=true'.format(i*44)
    data=r.urlopen(url).read().decode('utf-8')
    if data=='':
        continue
    import json
    data=json.loads(data)
    for j in range(len(data['mods']['itemlist']['data']['auctions'])):
        b=data['mods']['itemlist']['data']['auctions'][j]['view_price']
        f=str(b)
        ls.append(f)
mode(ls)

########################求众数第三种方法（网上找的函数）
import csv
with open('C:/Users/Administrator/Desktop/c.csv','r') as csvfile:
    reader=csv.reader(csvfile)
    column=[row[1] for row in reader]
print(column)

def get_mode(column):  
    mode = [];  
    column_appear = dict((a, column.count(a)) for a in column);  # 统计各个元素出现的次数  
    if max(column_appear.values()) == 1:  # 如果最大的出现为1  
        return;  # 则没有众数  
    else:  
        for k, v in column_appear.items():  # 否则，出现次数最大的数字，就是众数  
            if v == max(column_appear.values()):  
                mode.append(k);  
    return mode;  
print(get_mode(column))
#######################################
import numpy as np
np.mean(ls)##平均数
np.median(ls)##中位数