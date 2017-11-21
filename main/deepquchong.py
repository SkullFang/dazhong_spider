# -*- coding: utf-8 -*-
# @Time    : 2017/11/21 上午9:17
# @Author  : SkullFang
# @Email   : yzhang.private@gmail.com
# @File    : deepquchong.py
# @Software: PyCharm
import xlrd
import random
from xlwt import *
from urllib import request
from urllib.error import HTTPError,URLError
from bs4 import  BeautifulSoup
import socket

urlList=[]
stri = "../resouce/excel/allUrl.xls"
bk = xlrd.open_workbook(stri)
try:
    sh = bk.sheet_by_name("sheet1")
except:
    print("no sheet")

nrows = sh.nrows
ncols = sh.ncols
regs="^h.*[^#].*\d$"
for i in range(0, nrows):
    url = sh.cell_value(i, 1)
    if '#' not in url:
        print(str(i) + " " + url)
        urlList.append(url)

# 写入操作
w = Workbook(encoding="utf-8")
ws = w.add_sheet("sheet1", cell_overwrite_ok=True)
for i in range(len(urlList)):
    ws.write(i,0,i+1)
    ws.write(i, 1, urlList[i])

w.save("../resouce/excel/quchongURl.xls")
