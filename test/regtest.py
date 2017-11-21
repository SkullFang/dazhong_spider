# -*- coding: utf-8 -*-
# @Time    : 2017/11/21 上午9:21
# @Author  : SkullFang
# @Email   : yzhang.private@gmail.com
# @File    : regtest.py
# @Software: PyCharm
import re
# line =' "碧云路108号",'
line=' "HOODOGCAFE宠物咖啡(狗狗咖啡馆)",'
# line='"31.235457",'
# line="http://www.dianping.com/shop/24716347#promo=10524891"
regx="\s\" |.*\"([\u4E00-\u9fA5].* |[\w].*).*\""
match_obj=re.match(regx,line)
if match_obj is not None:
    print(match_obj.group(1))
else:
    print("Nope")