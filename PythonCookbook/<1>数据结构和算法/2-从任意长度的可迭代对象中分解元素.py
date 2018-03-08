# *表达式用来取全体值，来解决这个问题

grade = [45, 45, 45, 23, 35, 35, 54, 43, 43]

first, *middle, last = grade

print(first)
print(middle)
print(last)

# 这种方法对与不确定元素个数的序列来说很实用
# 下例无论有没有电话号码，phone_numbers都是一个列表
record = ('mike', 'dava@gmail.com', '158930483', '2440592042', '13549380289')
name, email, *phone_numbers = record
print(name)
print(email)
print(phone_numbers)

# *在对付变长的元组序列时十分有用，例如从命令行获取的*args

records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4)
]


def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

# 在做字符串拆分时也很有用

line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fileds, homedir, sh = line.split(':')
print(uname)
print(homedir)
print(sh)

# 当然你也可以选择用这种方法去忽略一部分值

record = ('ACEM', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
print(name)
print(year)
