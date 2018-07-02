# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 10:49:37 2018

爬取百度网页数据，用http:// 而不是其他
题目十一：爬取百度网页数据
1.爬取百度搜索标题
2.爬取标题下的描述
3.搜索的标题的网站
@author: Administrator
"""

#############################################3#######习题十一  百度网页
import urllib.request as r#导入联网工具包，命令为r  python
url='http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=python&oq=jay%2520chou&rsv_pq=e07322ab00012f19&rsv_t=9db9SjfSTfq3l4SBVrEtNiuUPfCkOFSFzXxHXiUF9StT8auU3%2BYpFkIoOak&rqlang=cn&rsv_enter=1&rsv_sug3=33&rsv_sug1=33&rsv_sug7=101&bs=jay%20chou'
data=r.urlopen(url).read().decode('utf-8')
print(data)
import re
###############标题、描述、网址
ls1=re.compile('"title":"(.*?)"').findall(data)
for i in range(len(ls1)):
    print('标题：{}'.format(ls1[i]))
ls2=re.compile('<div class="c-abstract"(.*?)</div>').findall(data)
for j in range(len(ls2)):
    print('摘要：{}'.format(ls2[j]))
ls3=re.compile('<div class="f13"><a target="_blank" href="(.*?)" class="c-showurl" ').findall(data)
for k in range(len(ls3)):
    print('网址：{}'.format(ls3[k]))