# -*- coding: utf-8 -*
return_message = {'code': 0, 'msg': '', 'message': '', 'data': [
    {'id': 4782116, 'roomid': 763869, 'uid': 14540141, 'type': 1, 'adminid': 6903512,
     'block_end_time': '2020-05-11 20:16:00', 'ctime': '2020-05-07 16:16:00', 'msg': '', 'msg_time': '',
     'uname': 'kikikikikiwa', 'admin_uname': 'SEmmmer'},
    {'id': 4782114, 'roomid': 763869, 'uid': 113737490, 'type': 1, 'adminid': 6903512,
     'block_end_time': '2020-05-11 20:15:54', 'ctime': '2020-05-07 16:15:54', 'msg': '', 'msg_time': '',
     'uname': '神仙大总攻', 'admin_uname': 'SEmmmer'},
    {'id': 4781976, 'roomid': 763869, 'uid': 544906812, 'type': 1, 'adminid': 6903512,
     'block_end_time': '2020-05-11 19:37:48', 'ctime': '2020-05-07 15:37:48', 'msg': '', 'msg_time': '',
     'uname': 'bili_41042354799', 'admin_uname': 'SEmmmer'}]}

block_man = return_message["data"][1]["uid"]

print(block_man)
