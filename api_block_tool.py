def ban_user(user, room_id: int, uid: int, hour: int):
    url = '//api.live.bilibili.com/banned_service/v2/Silent/add_block_user'
    data = {
        'roomid': room_id,
        'block_uid': uid,
        'hour': hour,
        'csrf_token': ,
        'csrf': ,
    }
    json_rsp = await user.other_session.request_json('POST', url, data=data, headers=user.dict_bili['pcheaders'])
    return json_rsp
