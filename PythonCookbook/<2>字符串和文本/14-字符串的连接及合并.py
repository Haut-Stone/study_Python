'''
用小字符串合并成一个大的字符串
'''


parts = ['Is', 'Chicago', 'Not', 'Chicago?']
print(' '.join(parts))
print(','.join(parts))
a = 'Is Chicago'
b = 'Not Chicago'
print(a + ' ' + b)

# 实际上字符串连接是很有学问的


s = ''
for part in parts:
    s += part  # 缓慢低效的
print(s)


# 下面的方法会更好一点
data = ['ACME', 50, 91.1]
print(','.join(str(d) for d in data))


c = 'nihao'

# 观察一下的几种字符串连接方式
print(a + ':' + b + ':' + c)  # ulgy
print(':'.join([a, b, c]))  # ulgy
print(a, b, c, sep=':')  # better


def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago?'


def combine(source, maxsize):
    parts = []
    size = 0
    for part in source:
        parts.append(part)
        size += len(part)
        if size > maxsize:
            yield ''.join(parts)
            parts = []
            size = 0
    yield ''.join(parts)

for part in combine(sample(), 510):
    print(part)
