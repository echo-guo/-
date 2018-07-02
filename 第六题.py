# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 10:39:27 2018

练习六：获取淘宝数据并且展示(只要第一页的商品48个)
1.每一行显示4个商品信息(商品名，价格，付款，店铺名,地址，)
2.列出12排商品
3.给商品排序，从价格高到低
4.给商品排序，按照销量排序
5.商品过滤，只要15天退款的商品，包邮的商品

@author: Administrator
"""
import urllib.request as r#导入联网工具包，命令为r
url='https://s.taobao.com/search?q=%E8%A3%A4%E5%AD%90&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&s=44&ajax=true'
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)
#data字典-》mods 字典-》itemlist 字典-》data字典-》auctions 列表-》index 0 字典-》raw_title 变量

#地址
#####################################
#第一二题
for i in range(0,44):
    a=data['mods']['itemlist']['data']['auctions'][i]['raw_title']
    b=data['mods']['itemlist']['data']['auctions'][i]['view_price']
    c=data['mods']['itemlist']['data']['auctions'][i]['nick']
    d=data['mods']['itemlist']['data']['auctions'][i]['item_loc']
    print('商品名：{}  价格为：{}  店铺名为：{}  地址为：{}'.format(a,b,c,d))
######################################
#第三问：价格排序
ls=[]
for i in range(1,44):
    b=data['mods']['itemlist']['data']['auctions'][i]['view_price']
    e=float(b)
    ls.append(e)
    sorted(ls)
    ls1=sorted(ls,reverse=True)
    print(ls1)

##################################
#第四问：销量排序
import re
ls=[]
for i in range(1,44):
    f=data['mods']['itemlist']['data']['auctions'][i]['view_sales']
    f1=re.sub("\D","",f)
    f2=int(f1)
    ls.append(f2)
    sorted(ls)
    ls1=sorted(ls,reverse=True)
    print(ls1)
#ls=sorted(ls)#正序
#############################
#第五问：商品过滤
for i in range(0,44):
    a=data['mods']['itemlist']['data']['auctions'][i]['raw_title']
    g=data['mods']['itemlist']['data']['auctions'][i]['view_fee']
    if g=='0.00':
        print('商品名:{}  包邮'.format(a))

