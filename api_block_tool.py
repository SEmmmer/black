# -*- coding: utf-8 -*
import me
import json
import requests

url = "http://api.live.bilibili.com/liveact/ajaxGetBlockList" + "?roomid=763869" + "&page=1" + "&csrf=bfd59952c846182dcaf59aad5bacba75" + "&csrf_token=bfd59952c846182dcaf59aad5bacba75"
cookies = me.cookie

code = requests.get(url, cookies=cookies)
text = json.loads(code.text)
print(text['data'])
