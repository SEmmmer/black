# -*- coding: utf-8 -*
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
data_base = client['test']
question = data_base['question']

question_file = open("file2.txt", "r")
for line in question_file:
    if line[0] != '1':
        continue
    array = line.split(':', 2)

    insert = True
    doc = {
        "uid": array[1],
        "danmaku": array[2],
        "finish": "no"
    }

    for result in question.find({"danmaku": array[2]}):
        insert = False

    if insert:
        question.insert(doc)
question_file.close()
