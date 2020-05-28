file = open("NLP/userdict.txt", "r")
names = []
for line in file:
    line = line.replace("\n", "").lower()
    if line not in names:
        names.append(line)
for one in names:
    print(one)
