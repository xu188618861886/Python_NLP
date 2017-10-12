#使用jieba先对中文表格文档进行分词处理
import jieba.analyse

wf = open('C:\\Users\\applee\\Desktop\\abc.txt', 'w+')
for line in open('C:\\Users\\applee\\Desktop\\123.csv'):
    item = line.strip('\n\r').split('\t')   #制表格切分
    print (item[0])
    tags = jieba.analyse.extract_tags(item[0])   #jieba分词
    tagsw = ",".join(tags)   #逗号连接切分的词
    wf.write(tagsw)

wf.close()
