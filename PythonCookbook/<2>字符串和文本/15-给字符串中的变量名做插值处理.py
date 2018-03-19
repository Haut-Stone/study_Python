'''
用变量来替换字符串中的部分内容
'''
import sys


# 用format来解决
s = '{name} has {n} messages.'
print(s.format(name='shi', n=37))


# 用format_map()和vars()来解决

name = 'li'
n = 43
print(s.format_map(vars()))  # 这就很微妙了


# vars()也可以用在类实例上


class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n

a = Info('nihao', 34)
print(s.format_map(vars(a)))  # 这说明其实变量也是在一个隐形字典中的。

# 但是如果有缺值的情况， 需要手工的添加一个__missing__方法


class safesub(dict):
    '''
    继承自字典
    '''
    def __missing__(self, key):
        return '{' + key + '}'

del n
print(s.format_map(safesub(vars())))

# 介绍一下frame hack技巧, 不得不说这个技巧看起来就有点专业了


def sub(text):
    return text.format_map(safesub(sys._getframe(1).f_locals))

name = 'LIsan'
n = 37
print(sub('Hello {name}'))
print(sub('You have {n} messages'))
print(sub('your favorite color is {color}'))
