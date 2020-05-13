# -*— coding: utf-8 -*
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
data_base = client['test']

col = data_base.get_collection('uid')
uid_list = col.find()
for i in uid_list:
    print(i)
