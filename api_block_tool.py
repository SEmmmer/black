# -*- coding: utf-8 -*
import me
import json
import requests

block_list = "http://api.live.bilibili.com/liveact/ajaxGetBlockList" + "?roomid=763869" + "&page=1" + f"&csrf={me.user['CSRF']}" + f"&csrf_token={me.user['CSRF']}"
cookies = me.cookie

get_list = requests.get(block_list, cookies=cookies)
return_message = json.loads(get_list.text)
block_man = return_message["data"][0]["uid"]

print(block_man)

block_url = "https://api.live.bilibili.com/banned_service/v2/Silent/add_block_user"
headers = {"content-type": "application/x-www-form-urlencoded"}
data = f"roomid=763869&block_uid=544906812&hour=1&csrf_token={me.user['CSRF']}&csrf={me.user['CSRF']}&visit_id="

block_it = requests.post(block_url, data=data, cookies=cookies, headers=headers)
return_message = json.loads(block_it.text)
print(return_message)
