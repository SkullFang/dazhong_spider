# -*- coding: utf-8 -*-
# @Time    : 2017/11/20 下午10:13
# @Author  : SkullFang
# @Email   : yzhang.private@gmail.com
# @File    : quchong.py
# @Software: PyCharm
import xlrd
import random
from xlwt import *
from urllib import request
from urllib.error import HTTPError,URLError
from bs4 import  BeautifulSoup
import socket

urlList = []
for j in range(1,19):
    stri="../resouce/excel/url"+str(j)+".xls"
    bk = xlrd.open_workbook(stri)
    try:
        sh = bk.sheet_by_name("sheet1")
    except:
        print("no sheet")

    nrows = sh.nrows
    ncols = sh.ncols



    for i in range(0, nrows):
        url = sh.cell_value(i, 1)
        print(str(i)+" "+url)
        urlList.append(url)



urlSet = set(urlList)

new_list=[]
for str in urlSet:
    new_list.append(str)

# 写入操作
w = Workbook(encoding="utf-8")
ws = w.add_sheet("sheet1", cell_overwrite_ok=True)
for i in range(len(new_list)):
    ws.write(i,0,i+1)
    ws.write(i, 1, new_list[i])


w.save("../resouce/excel/allUrl.xls")