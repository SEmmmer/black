# -*- coding: utf-8 -*


black = []
white = []
time = 0
# -----------------------------------
white_file = open("white.txt", "r")
for line in white_file:
    line = line.split()
    white.append(line[0])
white_file.close()

black_file = open("black.txt", "r")
for line in black_file:
    line = line.split()
    black.append(line[0])
black_file.close()
# -------------------------------------

file = open("file.txt", "r")
for line in file:
    if line[0] == "T":
        continue

    try:
        array = line.split(":", 2)
        time += 1
        if (array[1] not in black) and (array[1] not in white):

            print(time, "请判断该弹幕是否为引战弹幕，是请输入1，不是请直接回车")
            print(array[2])
            string = input()
            if string == "1":
                black.append(array[1])
            else:
                white.append(array[1])
        else:
            continue
    except (KeyboardInterrupt, IndexError):
        break

file.close()

black_file = open("black.txt", "w")
for uid in black:
    black_file.writelines(uid + "\n")
black_file.close()

while_file = open("white.txt", "w")
for uid in white:
    while_file.writelines(uid + "\n")
while_file.close()
