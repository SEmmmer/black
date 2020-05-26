from pypinyin import lazy_pinyin

file = open("words_only.txt", "r")
file_2 = open("words_only_pinyin.txt", "w")

for line in file:
    string = ""
    pin_yin = lazy_pinyin(line)
    for word in pin_yin:
        string += word[0]

    file_2.writelines("\n" + string + "\n")
    file_2.writelines(line + "\n")
file.close()
file_2.close()
