'''
简单用str.replace， 复杂用re
'''


import re
from calendar import month_abbr


text = 'nihao, This is my sakura block, 11/11/2012 todoganaikoi'
print(text.replace('my', 'your'))  # 这是一次性的，不改变原文本

# 复杂一点的就要用re了

print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))

# 如果要多次的话，你也可以先吧模式编译了

date_replacer = re.compile(r'(\d+)/(\d+)/(\d+)')
print(date_replacer.sub(r'\3-\1-\2', text))

# 对于更加复杂的情况，何以指定一个回调函数


def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))

print(date_replacer.sub(change_date, text))

text = '11/11/2012, dsaf m adsf m a 5/5/2015'
newtext, n = date_replacer.subn(r'\3-\1-\2', text)
print(newtext)
print(n)
