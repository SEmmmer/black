# -*- coding: utf-8 -*
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
data_base = client['test']

try:
    while True:
        question = data_base.get_collection('question')
        black = data_base.get_collection('uid')
        uid_list = black.find()
        single = question.find_one()
        print('请问该言论是否引战，是请输入1，否请直接回车：')
        print(single['danmaku'])
        string = input()
except KeyboardInterrupt:
    print("用户终止进程")
