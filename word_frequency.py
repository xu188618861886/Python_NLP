#承接tokenizer_jieba.py
#统计词频

#!/usr/bin/python
# -*- coding:utf-8 -*-

word_lst = []
word_dict = {}
with open('C:\\Users\\applee\\Desktop\\abc.txt') as wf, open("C:\\Users\\applee\\Desktop\\word.txt", 'w') as wf2:  #打开文件

    for word in wf:
        word_lst.append(word.split(',')) #使用逗号进行切分
        for item in word_lst:
            for item2 in item:
                if item2 not in word_dict: #统计数量
                    word_dict[item2] = 1
                else:
                    word_dict[item2] += 1
    for key in word_dict:
        print(key, word_dict[key])
        wf2.write(key + ' ' + str(word_dict[key]) + '\n') #写入文档

