# -*- coding: utf-8 -*
import me
import json
import requests

url = "http://api.live.bilibili.com/liveact/ajaxGetBlockList"
url2 = "http://api.live.bilibili.com/banned_service/v2/Silent/add_block_user"

cookies = me.cookie

requestData = {

    "roomid": 763869,
    # "block_uid": 544906812,
    "page": 1
    # "hour": 70,
    # "csrf": me.user["CSRF"],
    # "csrf_token": me.user["CSRF"],
    # "visit_id": 0
}

code = requests.post(url, data=json.dumps(requestData), cookies=cookies)
text = json.loads(code.text)
print(text)
