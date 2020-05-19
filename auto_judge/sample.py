# -*- coding: utf-8 -*-

import asyncio
import json

import requests

from auto_judge import blivedm
from threading import Thread
import me


def set_block_user(room_id, csrf, user_uid):
    block_url = "https://api.live.bilibili.com/banned_service/v2/Silent/add_block_user"
    headers = {"content-type": "application/x-www-form-urlencoded"}
    data = f"roomid={room_id}&block_uid={user_uid}&hour=720&csrf_token={csrf}&csrf={csrf}&visit_id="
    block_it = requests.post(block_url, data=data, cookies=cookies, headers=headers)
    return json.loads(block_it.text)


class MyBLiveClient(blivedm.BLiveClient):
    # 演示如何自定义handler
    _COMMAND_HANDLERS = blivedm.BLiveClient._COMMAND_HANDLERS.copy()

    async def _on_receive_danmaku(self, danmaku: blivedm.DanmakuMessage):
        black_word = {"sb", "yygq"}
        if danmaku.msg_type == 0:
            danmaku_content = f'{danmaku.timestamp}:{danmaku.uid}:{danmaku.msg}\n'
            print(danmaku_content)
            for one in black_word:
                if one in danmaku.msg:
                    c = BackBlock()
                    t = Thread(target=c.run, args=(room, my_csrf, danmaku.uid))
                    t.start()


class BackBlock:
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self, roomId, csrf, uid):
        while self._running:
            if set_block_user(roomId, csrf, uid)['code'] == -400:
                self._running = False


async def main():
    # 参数1是直播间ID
    # 如果SSL验证失败就把ssl设为False
    client = MyBLiveClient(763869, ssl=True)
    future = client.start()
    try:
        await future
    finally:
        await client.close()


if __name__ == '__main__':
    room = 763869
    cookies = me.cookies
    my_csrf = cookies['bili_jct']
    asyncio.get_event_loop().run_until_complete(main())
