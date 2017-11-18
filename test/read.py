# -*- coding: utf-8 -*-
# @Time    : 2017/11/18 下午3:57
# @Author  : SkullFang
# @Email   : yzhang_wy@163.com
# @File    : read.py
# @Software: PyCharm
import re
lines = None
with open('../resouce/url1.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

m = re.compile(r'')
matches = ['fullName','address', 'shopGlat', 'shopGlng',]

for line in lines:
    results = []
    keyword = line.strip().split(':')[0]
    # print(keyword)
    if keyword in matches:
        results.append(line.strip().split(':')[1])
    if results:
        print(results)