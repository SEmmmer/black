from gensim.models import Word2Vec

trained_module = Word2Vec.load("new_module")
test_words = ["114", "514", "夸哥", "算了", "apex", "孩子", "休息", "debu"]
length = len(test_words)
for i in range(length):
    res = trained_module.most_similar(test_words[i])
    print(test_words[i])
    print(res)
