'''
比如说空格符
'''

import re


s = ' hello world \n'
print(s.strip())  # 默认貌似是看不见的字符都去掉？但是只能去掉两端的
print(s.lstrip())
print(s.rstrip())

t = '------hello= = =='
print(t.strip('-='))


# 想要对句中的字符做处理，要换另外一种方法

s = '  hello   world    \n'
s = s.strip()
print(s.replace(' ', ''))
print(re.sub('\s+', ' ', s))


# 当然这也相当于一种数据处理，可以放在生成器中来进行

with open('test.txt') as f:
    lines = (line.strip() for line in f)
    for line in lines:
        print(line)
