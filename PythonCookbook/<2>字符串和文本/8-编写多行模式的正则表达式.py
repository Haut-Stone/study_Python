'''

'''

import re


comment = re.compile(r'/\*(.*?)\*/')
text1 = '/* this is a comment */'
text2 = '''
    /* this is a
       multiline comment */
'''

print(comment.findall(text1))
print(comment.findall(text2))  # 换行无法被匹配


# 为了解决这个问题，添加对换行符的支持,然而这并不好阅读，

comment = re.compile(r'/\*((?:.|\n)*?)\*/')
print(comment.findall(text2))

# 这里有一个有用的标记，可直接完成这个功能

comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)
print(comment.findall(text2))
