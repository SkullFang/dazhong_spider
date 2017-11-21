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
matches = ['fullName','address', 'shopGlat', 'shopGlng','mainCategoryName']
regx="\s\" |.*\"([\u4E00-\u9fA5].* |[\w].*).*\""
for line in lines:
    results = []
    keyword = line.strip().split(':')[0]
    # print(keyword)
    if keyword in matches:
        str=line.strip().split(':')[1]
        # print(str)
        match_obj = re.match(regx, str)
        if match_obj is not None:
            # print(match_obj.group(1))
            results.append(match_obj.group(1))
        else:
            print("Nope")

    if results:
        print(results)