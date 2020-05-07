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

block_url = "https://api.live.bilibili.com/banned_service/v2/Silent/add_block_user" + "?roomid=763869" + f"&block_uid={block_man}" + "&hour=720" + f"&csrf={me.user['CSRF']}" + f"&csrf_token={me.user['CSRF']}"
print(block_url)
block_it = requests.post(block_url, cookies=cookies)
return_message = json.loads(block_it.text)
print(return_message)
