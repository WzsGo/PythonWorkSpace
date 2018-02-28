#-*- coding=utf-8 -*-
import re

#创建一个 正则表达式 对象
#筛选小数类型的数据
#表达式中不能有 空格
patter = re.compile('\d+\.+\d+')

#定义需要筛选的文本
src = "1.23, 13, abc, 3.14"

#进行匹配，并得到结果
result = patter.findall(src)

#打印结果
print src
print result
for res in result:
	print res
