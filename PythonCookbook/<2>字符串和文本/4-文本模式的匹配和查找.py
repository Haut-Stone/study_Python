'''

'''

import re


text = 'yeah, but no, but yeah, but no, but yeah'
print(text == 'yeah')
print(text.startswith('yeah'))

# 这个find相较于C++就简单很多了
print(text.find('no'))

# 对于更复杂的匹配，我们就要用到re模块了

text1 = '11/27/2012'
text2 = 'Nov 27, 2012'
if re.match(r'\d+/\d+/\d+', text1):
    print('yes')
else:
    print('no')

# 如果打算做多次匹配，就吧正则表达式模式预编译成一个模式对象

datepat = re.compile(r'\d+/\d+/\d+')
if datepat.match(text2):
    print('yes')
else:
    print('no')

# 要找到所有的话就用findall

text = 'Today is 11/27/2012. pyCon starts 3/13/2013'
print(datepat.findall(text))


# 舍置捕获组会更加利于以后的使用

datepat2 = re.compile(r'(\d+)/(\d+)/(\d+)')  # 三个捕获组， 分别捕获3个数字
a = datepat2.match('11/12/2012')
print(a)
for num in range(4):
    print(a.group(num))

print(a.groups())  # 注意是groups不是group
day, month, year = a.groups()


