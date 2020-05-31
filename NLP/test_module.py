from gensim.models import Word2Vec

trained_module = Word2Vec.load("NLP/danmaku_module")
test_words = ["dd",
              "可乐"
              # "夏哥",
              # "电脑",
              # "呼吸",
              # "holo",
              # "血压",
              # "游戏"
              ]
length = len(test_words)
for i in range(length):
    res = trained_module.most_similar(test_words[i])
    print(test_words[i])
    print(res)
