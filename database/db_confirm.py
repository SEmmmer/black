# -*- coding: utf-8 -*
import pymongo
import confirm

black = []
client = pymongo.MongoClient("mongodb://localhost:27017/")
data_base = client['test']

uid_col = data_base.get_collection('uid')
uid_list = uid_col.find({'type': "black"})
for uid in uid_list:
    black.append(uid['uid'])
print(black)

file = open("confirm_list.txt", "a")
confirm.c_out()
print("over")
file.close()
