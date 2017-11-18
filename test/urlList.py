# -*- coding: utf-8 -*-
# @Time    : 2017/11/16 下午8:38
# @Author  : SkullFang
# @Email   : yzhang_wy@163.com
# @File    : urlList.py
# @Software: PyCharm

from urllib import request
from urllib.error import HTTPError,URLError
from bs4 import  BeautifulSoup
import datetime
import re
from xlwt import *
import socket

# print(i)
url="http://www.dianping.com/search/keyword/1/0_%E5%92%96%E5%95%A1%E5%8E%85/r5p3?aid=75092761%2C66832113"
try:
    re1 = request.Request(url)
    # 把爬虫伪装成浏览器
    re1.add_header('user-agent',
                   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36')
    req = request.urlopen(re1, timeout=200)
except (HTTPError, URLError, ConnectionResetError, socket.timeout) as e:
    print("error")# 遇到相应错误就跳过

try:
    soup = BeautifulSoup(req.read().decode("utf-8"), "html.parser")  # 指定解析器
    # print(soup)
    ListUrls=soup.findAll("a",href=re.compile('(.+)(shop)(.+)\d$'))
    for list in ListUrls:
        print(list["href"])





except (AttributeError, HTTPError, URLError, ConnectionResetError, socket.timeout) as e:
    print(e)