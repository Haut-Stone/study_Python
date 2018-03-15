'''
用变量来替换字符串中的部分内容
'''


# 用format来解决
s = '{name} has {n} messages.'
print(s.format(name='shi', n=37))


# 用format_map()和vars()来解决

name = 'li'
n = 43
print(s.format_map(vars()))  # 这就很微妙了

vars()
