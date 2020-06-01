import os
import re
import jieba.analyse

RAW_PATH = "/Users/yangjinghua/bilibili-vtuber-danmaku/"

if_go = input("你确定？")
if if_go != "yes":
    exit(1)

jieba.analyse.set_stop_words("NLP/stopwords")
jieba.load_userdict("NLP/userdict.txt")

sum_file = open("/Volumes/双皮奶/danmaku/whole_danmaku.txt", "w")
for i in range(22261335):
    PATH = RAW_PATH + str(i) + "/"
    if not os.path.exists(PATH):
        continue
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
                    file = open(PATH + filename, "r", encoding="utf-8")
                    try:
                        for line in file:
                            if line[0] != "1":
                                continue
                            danmaku = line.split(":", 2)
                            if len(danmaku) < 3:
                                continue
                            danmaku = danmaku[2].lower().replace("\n", "").replace(' ', "")

                            res = re.search("n.e{1,30}e", danmaku)
                            if res:
                                danmaku = danmaku.replace(res.group(), "nee")

                            res = re.search("m.o{1,30}o", danmaku)
                            if res:
                                danmaku = danmaku.replace(res.group(), "moo")

                            res = re.search("2.3{1,30}3", danmaku)
                            if res:
                                danmaku = danmaku.replace(res.group(), "233")

                            res = re.search("([啊阿a])([我维w伟]).{0,10}([死睡s])([了l])", danmaku)
                            if res:
                                danmaku = danmaku.replace(res.group(), "awsl")

                            res = re.search("我(兄弟|朋友).{0,10}好了", danmaku)
                            if res:
                                danmaku = danmaku.replace(res.group(), "whl")

                            res = re.search("好([色])哦", danmaku)
                            if res:
                                danmaku = danmaku.replace(res.group(), "hso")

                            res = re.search("(.()+)\\1{3,}", danmaku)
                            if res:
                                single_words = res.group()[0:3]
                                danmaku = danmaku.replace(res.group(), single_words)

                            danmaku = danmaku.replace("待機", "待机")
                            danmaku = danmaku.replace("ここすき", "kksk")
                            danmaku = danmaku.replace("kokosuki", "kksk")
                            danmaku = danmaku.replace("cocosuki", "kksk")
                            danmaku = danmaku.replace("ここ好き", "kksk")

                            seg_list = jieba.analyse.extract_tags(danmaku)
                            output = " ".join(seg_list) + " "
                            sum_file.writelines(output)
                    except UnicodeDecodeError:
                        continue
                    file.close()
            day = 1
        month = 1

sum_file.close()
