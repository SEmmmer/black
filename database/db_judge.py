# -*- coding: utf-8 -*
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
data_base = client['test']

try:
    while True:
        question = data_base.get_collection('question')
        uid_col = data_base.get_collection('uid')
        uid_list = uid_col.find()
        single = question.find_one()
        if single['uid'] not in uid_list:
            print('请问该言论是否引战，是请输入1，否请直接回车：')
            print(single['danmaku'])
            string = input()

            if string == '1':
                doc = {"uid": single['uid'], "type": "black"}
                uid_col.insert_one(doc)
            else:
                doc = {"uid": single['uid'], "type": "white"}
                uid_col.insert_one(doc)

        question.delete_one(single)
        # 处理完该问题
        # 从弹幕库中删除

except KeyboardInterrupt:
    print("用户终止进程")
