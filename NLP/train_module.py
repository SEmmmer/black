import multiprocessing
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
import time

string = input("为了防止重复运行覆盖数据，请输入1后回车来启动训练")
if string != "1":
    exit(1)

input_file = open("./whole_danmaku.txt", "rb")
out_module = open("./danmaku_module", "wb")
out_vec = open("./danmaku_vec", "wb")

model = Word2Vec(
    LineSentence(input_file),
    size=512,
    window=3,
    min_count=3,
    workers=multiprocessing.cpu_count(),
    sg=0
)
model.save(out_module)

model.wv.save_word2vec_format(out_vec, binary=False)
print(time.ctime())
