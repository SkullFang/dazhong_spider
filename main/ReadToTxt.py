# -*- coding: utf-8 -*-
# @Time    : 2017/11/21 上午9:34
# @Author  : SkullFang
# @Email   : yzhang.private@gmail.com
# @File    : ReadToTxt.py
# @Software: PyCharm
from urllib import request
from urllib.error import HTTPError,URLError
from bs4 import  BeautifulSoup
import datetime
import re
from xlwt import *
import xlrd
import socket
import time
stri = "../resouce/excel/quchongURl.xls"
bk = xlrd.open_workbook(stri)
try:
    sh = bk.sheet_by_name("sheet1")
except:
    print("no sheet")

nrows = sh.nrows
ncols = sh.ncols
regs="^h.*[^#].*\d$"
for i in range(0, 1001):
    url = sh.cell_value(i, 1)
    time.sleep(1)
    if '#' not in url:
        try:
            re1 = request.Request(url)
            # 把爬虫伪装成浏览器
            re1.add_header('user-agent',
                           'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36')
            re = request.urlopen(re1, timeout=200)
        except (HTTPError, URLError, ConnectionResetError, socket.timeout) as e:
            print("error head")  # 遇到相应错误就跳过

        try:
            soup = BeautifulSoup(re.read().decode("utf-8"), "html.parser")  # 指定解析器
            # print(soup)
            # title = soup.findAll("h1")
            # rtitle = title[0].get_text()
            # print(rtitle)
            # for t in title:
            #     print(t.get_text())
            print(i)

            with open("../resouce/txt/url"+str(i)+".txt", "w") as f:
                f.write(str(soup))
        except (AttributeError, HTTPError, URLError, ConnectionResetError, socket.timeout) as e:
            print("error")


