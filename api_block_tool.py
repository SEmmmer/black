# -*- coding: utf-8 -*
import me
import json
import requests

block_list = "http://api.live.bilibili.com/liveact/ajaxGetBlockList" + "?roomid=763869" + "&page=1" + f"&csrf={me.user['CSRF']}" + f"&csrf_token={me.user['CSRF']}"
cookies = me.cookie

code = requests.get(block_list, cookies=cookies)
text = json.loads(code.text)
block_man = text["data"][0]["uid"]

print(block_man)

url2 = "https://api.live.bilibili.com/banned_service/v2/Silent/add_block_user" + "?roomid=763869" + f"&block_uid={block_man} " + "&hour=720" + f"&csrf={me.user['CSRF']}" + f"&csrf_token={me.user['CSRF']}"

