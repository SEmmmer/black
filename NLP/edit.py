import re
import jieba.analyse

jieba.analyse.set_stop_words("NLP/stopwords")
jieba.load_userdict("NLP/userdict.txt")

file = open("NLP/file2.txt", "r")
new_file = open("NLP/sum_file.txt", "w")
for line in file:
    if line[0] != "1":
        continue
    danmaku = line.replace("\n", "").split(":", 2)[2].lower()

    res = re.search("n.e{1,30}e", danmaku)
    if res:
        danmaku = danmaku.replace(res.group(), "nee")

    res = re.search("m.o{1,30}o", danmaku)
    if res:
        danmaku = danmaku.replace(res.group(), "moo")

    res = re.search("2.3{1,30}3", danmaku)
    if res:
        danmaku = danmaku.replace(res.group(), "233")

    res = re.search("(啊|阿|a)(我|维|w|伟).{0,10}(死|睡|s)(了|l)", danmaku)
    if res:
        danmaku = danmaku.replace(res.group(), "awsl")

    res = re.search("我(兄弟|朋友).{0,10}好了", danmaku)
    if res:
        danmaku = danmaku.replace(res.group(), "whl")

    res = re.search("好(色|帅)哦", danmaku)
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
    output = "/".join(seg_list) + "\n"
    new_file.writelines(output)
