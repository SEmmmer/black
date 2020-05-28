import os
import sys
import multiprocessing
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence

a = input("are you sure")
if a != "yes":
    exit(1)

input_file = open("sum_file.txt", "rb")
out_module = open("new_module", "wb")
out_vec = open("new_vec", "wb")
model = Word2Vec(LineSentence(input_file), size=512, window=2, min_count=3, workers=multiprocessing.cpu_count())
model.save(out_module)

model.wv.save_word2vec_format(out_vec, binary=False)
