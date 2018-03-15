'''

'''

import re


text = 'UPPER PYTHON, lower python, Mixed Python'
a = re.findall('python', text, flags=re.IGNORECASE)  # 无视大小写
print(a)
b = re.sub('python', 'snake', text, flags=re.IGNORECASE)  # 无视大小写替换
print(b)

# 但是问题是替换的文本和原来的文本是不匹配的，这里就要用到，一个支撑函数


# 这个替换函数没太看懂啊
def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace

print(re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE))
