# -*- coding: utf-8 -*
from bilibili_api import Verify
from bilibili_api.user import UserOperate

verify = Verify(sessdata="your sessdata", csrf="your csrf")
# 请务必不要泄漏这两项数据

file = open("black.txt", "r")

for line in file:
    line = line.split()
    uid = int(line[0])
    user = UserOperate(uid=uid, verify=verify)
    user.set_black()
    print("目标", str(uid), "已经被清除")
print("程序结束")
