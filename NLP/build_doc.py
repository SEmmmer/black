import os
import jieba.analyse

PATH = "/Users/yangjinghua/bilibili-vtuber-danmaku/14917277/"

if_go = input("你确定？")
if if_go != "yes":
    exit(1)

jieba.analyse.set_stop_words("NLP/stopwords")
jieba.load_userdict("NLP/userdict.txt")
sum_file = open("NLP/sum_file.txt", "w")

for n in range(2):
    year = 2019 + n
    for y in range(12):
        month = 1 + y
        for t in range(31):
            day = 1 + t

            date = [str(year), str(month), str(day)]
            filename = "-".join(date) + ".txt"
            if os.path.exists(PATH + filename):
                print(filename + " exist")
                file = open(PATH + filename, "r")
                for line in file:
                    if line[0] != "1":
                        continue
                    danmaku = line.split(":", 2)
                    if len(danmaku) < 3:
                        continue
                    seg_list = jieba.analyse.extract_tags(danmaku[2])
                    output = " ".join(seg_list) + " "
                    print(output)
                    sum_file.writelines(output)
                file.close()
        day = 1
    month = 1
sum_file.close()
