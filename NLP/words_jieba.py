# encoding=utf-8
import jieba

file = open("file2.txt", "r")
file_two = open("new.txt", "w")
jieba.load_userdict("userdict.txt")
for line in file:
    danmaku = line.split(":", 2)[2]
    seg_list = jieba.cut(danmaku.replace("\n", ""))
    result = "/".join(seg_list) + "\n"
    if '/' in result:
        file_two.writelines(result)
file_two.close()
file.close()
