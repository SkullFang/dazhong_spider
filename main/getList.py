# -*- coding: utf-8 -*-
# @Time    : 2017/11/18 下午4:11
# @Author  : SkullFang
# @Email   : yzhang_wy@163.com
# @File    : getList.py
# @Software: PyCharm
from urllib import request
from urllib.error import HTTPError,URLError
from bs4 import  BeautifulSoup
import datetime
import re
from xlwt import *
import socket
listStr=[]
lenth=0
# 写入操作
w = Workbook(encoding="utf-8")
ws = w.add_sheet("sheet1", cell_overwrite_ok=True)
for i in range(1,3):
    url = "http://www.dianping.com/search/keyword/1/0_%E5%92%96%E5%95%A1%E5%8E%85/c3580p"+str(i)
    try:
        re1 = request.Request(url)
        # 把爬虫伪装成浏览器
        re1.add_header('user-agent',
                       'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36')
        req = request.urlopen(re1, timeout=200)
    except (HTTPError, URLError, ConnectionResetError, socket.timeout) as e:
        i = i + 1
        continue
        print("error")  # 遇到相应错误就跳过

    try:
        soup = BeautifulSoup(req.read().decode("utf-8"), "html.parser")  # 指定解析器
        # print(soup)
        ListUrls = soup.findAll("a", href=re.compile('(.+)(shop)(.+)\d$'))
        for url in ListUrls:
            urli=url['href']
            print(str(i)+" "+urli)
            listStr.append(urli)
            lenth=lenth+1


    except (AttributeError, HTTPError, URLError, ConnectionResetError, socket.timeout) as e:
        i=i+1
        continue
        print(e)


for i in range(lenth):
    ws.write(i,0,i+1)
    ws.write(i, 1, listStr[i])


w.save("../resouce/excel/chongming.xls")