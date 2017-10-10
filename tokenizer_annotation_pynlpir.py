#分词并词性标注，利用中科院pynlpir
# pynlpir是一个针对中科院分词器NLPIR/ICTCLAS而开发的一个python包

# coding:utf-8

import pynlpir

pynlpir.open()
s = '聊天机器人到底该怎么做呢？'
segments = pynlpir.segment(s,pos_english=False)
for segment in segments:
    print (segment[0], '\t', segment[1])

pynlpir.close()

