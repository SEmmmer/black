# encoding=utf-8
import jieba.analyse
from nltk.stem.porter import *
from sklearn.feature_extraction.text import TfidfVectorizer

file = open("file2.txt", "r")
file_two = open("new.txt", "w")
jieba.load_userdict("userdict.txt")

# jieba.analyse.set_stop_words('stopwords')
#
# stemmer = PorterStemmer()
# vector = TfidfVectorizer(smooth_idf=False)
for line in file:
    danmaku = line.split(":", 2)[2]
    # seg_list = jieba.analyse.extract_tags(danmaku, 20)
    # seg_list = [stemmer.stem(word) for word in seg_list]
    seg_list = jieba.cut(danmaku)
    # if len(seg_list) < 2:
    #     continue
    # print(seg_list)
    # X = vector.fit_transform(seg_list)
    # print(X.toarray())
    # print(vector.get_feature_names())
    result = "/".join(seg_list)

    if '/' in result:
        file_two.writelines(result)
file_two.close()
file.close()
# file_thr.close()
