# -*- coding: utf-8 -*
import pymongo


def c_out():
    global line
    for man in black:
        file.writelines(str(man) + "\n")
        danmaku_file = open("file.txt", "r")
        for line in danmaku_file:
            array = line.split(":", 2)
            if int(array[1]) == int(man):
                puts = array[2].split()[0]
                file.writelines(puts + "\n")
        print("")
        file.writelines("\n")
        danmaku_file.close()


black = []
client = pymongo.MongoClient("mongodb://localhost:27017/")
data_base = client['test']

uid_col = data_base.get_collection('uid')
uid_list = uid_col.find({'type': "black"})
for uid in uid_list:
    black.append(uid['uid'])

file = open("confirm_list.txt", "a")
c_out()
print("over")
file.close()
