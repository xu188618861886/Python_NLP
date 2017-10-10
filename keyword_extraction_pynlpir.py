#中文关键词提取，利用中科院pynlpir
# pynlpir是一个针对中科院分词器NLPIR/ICTCLAS而开发的一个python包
# coding:utf-8

import pynlpir

pynlpir.open()
s = '聊天机器人到底该怎么做呢？'
print ('关键词测试:\n')
key_words = pynlpir.get_key_words(s, weighted=True)
for key_word in key_words:
    print (key_word[0], '\t', key_word[1])

pynlpir.close()
