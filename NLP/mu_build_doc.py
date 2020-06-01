import os
import re


async def find_dir(now_dir: int, raw_path: str) -> str:
    PATH = raw_path + str(now_dir) + "/"
    if not os.path.exists(PATH):
        return await find_dir(now_dir + 1, raw_path)
    else:
        return PATH


async def to_one_word():


if __name__ == "__main__":
    RAW_PATH = "/Users/yangjinghua/bilibili-vtuber-danmaku/"
    file = open("NLP/file.txt")
    for line in file:
        res = re.search("([kcこコ]){2}.{0,20}([sす好ス]).{0,20}([kきキ]).{0,20}", line)
        if res:
            print(res.group())
