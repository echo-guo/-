# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 10:32:20 2018

12306.cn火车票余票查询
中国铁路火车票上的车次，有以C（读作“城”）打头的车次、
以D（读作“动车”）打头的车次、
以G（读作“高”）打头的车次、-------------------------------OK
以N（读作“内”）打头的车次、
以Z（读作“直”）打头的车次、
以T（读作“特”）打头的车次、
以K（读作“快”）打头的车次、
以L（读作“临”）打头的车次、
以Y（读作“游”）打头的车次和不带字母打头的车次等十余种。
题目九：余票查询组项目
1.查询某种火车的余票，动车，高铁，直达，特快....
2.组长将各组员功能汇总

@author: Administrator
"""
import urllib.request as r#导入联网工具包，命令为r
url='https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2018-06-30&leftTicketDTO.from_station=XAY&leftTicketDTO.to_station=SHH&purpose_codes=ADULT'
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)
data=data['data']['result']

p='  '
s="v8hzesw92snv0p%2BXbBSYcvDvrkZJongII6gnHaa1K%2B5ZLSH2S1yiEmi5TocBRsVZ7KheRoWRj4s2%0AVRYp%2F1qQIXo6MxxZNB3giUuTVVn2qCjkK0zSOEIvJTiliIOKVW5rcQneIukZPdBmkyTOIosb%2FhFD%0AtpChpGqPNAY%2F29y3VTJO4Sh51LMePmFmF7Hv7THUyJDqN5VO5lYhnC611uP65vpluqQm243rAtJw%0AYiIa3SmEBr%2FXR331dZJkt7EmP3dw|预订|76000C630407|C6304|IXW|JFW|IVW|CNW|09:46|10:47|01:01|Y|NiY4S31uZETanTCgYyNeHA1zyfhqgCHmfzE%2B20yxLvYgcLOY|20180625|3|W1|02|06|1|0|||||||有||||无|无|||O0M0O0|OMO|0"
s=data[0]
ls=s.split('|')
len([p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p])
title='车次{}出发站/到达站{}出发时间/到达时间{}历时{}商务座/特等座{}一等座{}二等座{}高级软卧{}软卧{}动卧{}硬卧{}软座{}硬座{}无座{}其他{}备注'.format(p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p)
title=title.split(p)
for i in title:
    print(i.center(12),end='')
print()
#车次   车发站，到达站 出发时间,到达时间 历时间
ls=[ls[3],[ls[6],ls[7]],[ls[8],ls[9]],ls[10],ls[32],ls[31],ls[30],'--','--','--','--','--','--',ls[26],'--',ls[1]]
for i in ls:
    print(str(i).center(15).replace('[','').replace(']',''),end='')
