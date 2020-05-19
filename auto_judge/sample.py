# -*- coding: utf-8 -*-

import asyncio

from auto_judge import blivedm
import datetime
import os


class MyBLiveClient(blivedm.BLiveClient):
    # 演示如何自定义handler
    _COMMAND_HANDLERS = blivedm.BLiveClient._COMMAND_HANDLERS.copy()

    async def _on_receive_danmaku(self, danmaku: blivedm.DanmakuMessage):
        if danmaku.msg_type == 0:
            danmaku_content = f'{danmaku.timestamp}:{danmaku.uid}:{danmaku.msg}\n'
            print(danmaku_content)


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
    asyncio.get_event_loop().run_until_complete(main())
