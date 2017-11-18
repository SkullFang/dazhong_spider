# -*- coding: utf-8 -*-
# @Time    : 2017/11/18 下午3:53
# @Author  : SkullFang
# @Email   : yzhang_wy@163.com
# @File    : loadTxt.py
# @Software: PyCharm
from urllib import request
from urllib.error import HTTPError,URLError
from bs4 import  BeautifulSoup
import datetime
import re
from xlwt import *
import socket

# print(i)
url="http://www.dianping.com/shop/66832113"
try:
    re1 = request.Request(url)
    # 把爬虫伪装成浏览器
    re1.add_header('user-agent',
                   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36')
    re = request.urlopen(re1, timeout=200)
except (HTTPError, URLError, ConnectionResetError, socket.timeout) as e:
    print("error")# 遇到相应错误就跳过

try:
    soup = BeautifulSoup(re.read().decode("utf-8"), "html.parser")  # 指定解析器
    # print(soup)
    title = soup.findAll("h1")
    rtitle=title[0].get_text()
    print(rtitle)
    # for t in title:
    #     print(t.get_text())

    with open("../resouce/url1.txt","w") as f:
        f.write(str(soup))







except (AttributeError, HTTPError, URLError, ConnectionResetError, socket.timeout) as e:
    print("error")