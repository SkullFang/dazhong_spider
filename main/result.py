# -*- coding: utf-8 -*-
# @Time    : 2017/11/21 上午10:14
# @Author  : SkullFang
# @Email   : yzhang.private@gmail.com
# @File    : result.py
# @Software: PyCharm
import re
lines = None
for i in range(0,1001):
    stri="../resouce/txt/url"+str(i)+".txt"
    with open(stri, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    m = re.compile(r'')
    matches = ['fullName','address', 'shopGlat', 'shopGlng','mainCategoryName']
    regx="\s\" |.*\"([\u4E00-\u9fA5].* |[\w].*).*\""
    for line in lines:
        results = []
        keyword = line.strip().split(':')[0]
        # print(keyword)
        if keyword in matches:
            strlin=line.strip().split(':')[1]
            # print(str)
            match_obj = re.match(regx, strlin)
            if match_obj is not None:
                # print(match_obj.group(1))
                results.append(match_obj.group(1))
            else:
                print("Nope")

        if results:
            print(results)