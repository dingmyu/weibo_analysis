# -*- coding: utf-8 -*-
import pandas as pd
import re
import jieba
import jieba.analyse
from collections import Counter
import sys
import time
import jieba.posseg as pseg
import keywords_new
reload(sys)
sys.setdefaultencoding('utf-8')

#sentence = "用知识的浪花去推动思考的风帆，用智慧的火星去点燃思想的火花，用浪漫的激情去创造美好的生活，用科学的力量去强劲腾飞的翅膀！只有使自己自卑的心灵自信起来，弯曲的身躯才能挺直；只有使自己懦弱的体魄健壮起来，束缚的脚步才能迈开；只有使自己狭隘的心胸开阔起来，短视的眼光才能放远；只有使自己愚昧的头脑聪明起来，愚昧的幻想才能抛弃不点燃智慧的火花，聪明的头脑也会变为愚蠢；不践行确立的目标，浪漫的理想也会失去光彩；不珍惜宝贵的时间，人生的岁月也会变得短暂；不总结失败的经验，简单的事情也会让你办砸。宠爱的出发点是爱，落脚点却是恨；嫉妒的出发点是进，落脚点却是退；梦幻的出发点是绚（烂），落脚点却是空；贪婪的出发点是盈，落脚点却是亏。没有激情，爱就不会燃烧；没有友情，朋就不会满座；没有豪情，志就难于实现；没有心情，事就难于完成。我们缺少的不是机遇，而是对机遇的把握；我们缺欠的不是财富，而是创造财富的本领；我们缺乏的不是知识，而是学而不厌的态度；我们缺少的不是理想，而是身体力行的实践。有了成绩要马上忘掉，这样才不会自寻烦恼；有了错误要时刻记住，这样才不会重蹈覆辙；有了机遇要马上抓住，这样才不会失去机会；有了困难要寻找对策，这样才能迎刃而解。你可以不高尚，但不能无耻；你可以不伟大，但不能卑鄙；你可以不聪明，但不能糊涂；你可以不博学，但不能无知；你可以不交友，但不能孤僻；你可以不乐观，但不能厌世；你可以不慷慨，但不能损人；你可以不追求，但不能嫉妒；你可以不进取，但不能倒退。生活需要游戏，但不能游戏人生；生活需要歌舞，但不需醉生梦死；生活需要艺术，但不能投机取巧；生活需要勇气，但不能鲁莽蛮干；生活需要重复，但不能重蹈覆辙。把工作当享受，你就会竭尽全力；把生活当乐趣，你就会满怀信心；把读书当成长，你就会勤奋努力；把奉献当快乐，你就会慷慨助人。"

f = open("YOUR_USER_ID", "r")
f1 = open("category.txt", "w")
f2 = open("express.txt", "w")
f3 = open("word.txt", "w")
f4 = open("name.txt", "w")
list1 = []
record = {}  # 记录命中信息
express = {}
name_set = {}
while True:
    line = f.readline().strip().decode('utf-8')
    if line:
        item = line.split(' ', 1)[1]
        ex_all = re.findall(u"\\[.*?\\]", item)  
        if ex_all:
            for ex_item in ex_all:
                express[ex_item] = express.get(ex_item, 0) + 1
        for kw, keywords in keywords_new.keyword_dict.iteritems():  # kw是大类
            flag = 0  # 大类命中的标志
            for key, keyword in keywords.iteritems():  # key 是小类
            	if flag == 1:
            		break
                for word in keyword:  # 小类关键词
                    match_flag = 1  # 列表中关键词全部命中的标志
                    for small_word in word:  # 关键词列表
#                    	print small_word
                        match = re.search(re.compile(small_word, re.I), item)
                        if not match:
                            match_flag = 0
                            break
                    if match_flag == 1:  #命中了一个小类
                        record[kw] = record.get(kw, 0) + 1 # 单次记录
                        flag = 1
                        break
        item = re.sub(u"\\[.*?\\]", '', item)
        list = jieba.cut(item, cut_all = False)
        for ll in list:
            list1.append(ll)  # 分词
        seg_list = pseg.cut(item)
        for word, flag in seg_list:
            if flag == 'nr':
                name_set[word] = name_set.get(word, 0) + 1
    else:
        break

count = Counter(list1)
for item in sorted(dict(count).iteritems(), key=lambda d:d[1], reverse = True):
    if len(item[0]) >= 2 and item[1] >= 3:   
        print >> f3, item[0],item[1] 

for key, keywords in sorted(record.iteritems(), key=lambda d:d[1], reverse = True):
    print >> f1, u'命中了', key, record[key], u'次'

for key, keywords in sorted(express.iteritems(), key=lambda d:d[1], reverse = True):
    print >> f2, u'使用了', key, u'表情', express[key], u'次'

for key, keywords in sorted(name_set.iteritems(), key=lambda d:d[1], reverse = True):
    print >>f4, u'使用了名字', key, name_set[key], u'次'
