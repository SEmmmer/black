# -*- coding: utf-8 -*
import re
import os

black = []
white = []
for line in open("aaa.txt", "r"):
    try:
        array = line.split(":", 2)
        if (array[1] not in black) and (array[1] not in white):
            print("请判断该弹幕是否为引战弹幕，是请输入1，不是请直接回车")
            print(array[2])
            string = input()
            if string == "1":
                black.append(array[1])
            else:
                white.append(array[1])
        else:
            continue
    except KeyboardInterrupt:
        black_file = open("black.txt", "w")
        for uid in black:
            black_file.writelines(uid)


    else:
        print("over")
