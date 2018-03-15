'''

'''

import re


str_pat = re.compile(r'\"(.*)\"')
text1 = 'Computer says "no."'
print(str_pat.findall(text1))
text2 = 'Computer says "no." Phone says "yes."'
print(str_pat.findall(text2))  # 贪心的找了一整个字符串

# 可以加一个？来解决这个问题
str_pat = re.compile(r'\"(.*?)\"')
print(str_pat.findall(text2))
