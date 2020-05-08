# -*— coding: utf-8 -*
white_str = ["ぺこ", "待機", "待机", "O", "o", "k", "K", "草", "8888", "114", "大丈夫"]

with open('file.txt', 'r') as r:
    lines = r.readlines()
with open('file2.txt', 'w') as w:
    for l in lines:
        for word in white_str:
            if word in lines:
                continue
            continue

        print(l)
