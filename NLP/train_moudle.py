import multiprocessing
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
import time

input_file = open("/Volumes/双皮奶/danmaku/whole_danmaku.txt", "rb")
out_module = open("/Volumes/双皮奶/danmaku/danmaku_module", "wb")
out_vec = open("/Volumes/双皮奶/danmaku/danmaku_vec", "wb")
model = Word2Vec(LineSentence(input_file), size=512, window=3, min_count=3, workers=multiprocessing.cpu_count(), sg=0)
model.save(out_module)

model.wv.save_word2vec_format(out_vec, binary=False)
print(time.ctime())
