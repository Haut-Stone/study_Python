'''
普通的split（）方法较为局限，这里介绍一下re的split（）方法
'''


import re


line = 'asdf fjdk; afed, fjek,asdf,   foo'
a = re.split(r'[;,\s]\s*', line)  # \s是空白字符，这里代表空格
print(a)


# 用捕获组的话会产生另外一种效果

b = re.split(r'(;|,|\s)\s*', line)
print(b)

# 通过以下方式去掉分隔符

values = b[::2]
delimiters = b[1::2] + ['']
print(values)
print(delimiters)
print(''.join(v+d for v, d in zip(values, delimiters)))  # 还原字符串


# 不想获得分隔符的话用以下的方法

c = re.split(r'(?:;|,|\s)\s*', line)
print(c)
