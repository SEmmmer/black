# -*- coding: utf-8 -*
import sec
import bilibili_api.user
from bilibili_api import Verify
from bilibili_api.user import UserOperate

print(sec.file["CSRF"])
verify = Verify(sessdata="your sessdata", csrf="your csrf")
