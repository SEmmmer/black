
from threading import Thread
import me


def set_block_user(room_id, csrf, user_uid):
    block_url = "https://api.live.bilibili.com/banned_service/v2/Silent/add_block_user"
    headers = {"content-type": "application/x-www-form-urlencoded"}
    data = f"roomid={room_id}&block_uid={user_uid}&hour=720&csrf_token={csrf}&csrf={csrf}&visit_id="
    block_it = requests.post(block_url, data=data, cookies=cookies, headers=headers)
    return json.loads(block_it.text)


class BackBlock:
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self, roomId, csrf, uid):
        while self._running:
            if set_block_user(roomId, csrf, uid)['code'] == -400:
                self._running = False


room = 763869
cookies = me.cookies
my_csrf = cookies['bili_jct']

c = BackBlock()
t = Thread(target=c.run, args=(room, my_csrf, 123456))
t.start()
# c.terminate()
