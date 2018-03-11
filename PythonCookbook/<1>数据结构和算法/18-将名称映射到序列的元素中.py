'''
用命名元组，来代替下表，提高可读性
'''


from collections import namedtuple


Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')
print(sub)
print(sub.addr)


# namedtuple的类实例和元组是可以互换的

print(len(sub))
addr, joined = sub
print(addr)
print(joined)


# 命名元元组和普通元组的比较

records = [('ACMF', 5, 2.5), ('AECC', 3, 2.5)]


def compute_cost(records):
    total = 0.0
    for rec in records:
        total += rec[1] * rec[2]
    return total


def compute_cost2(records):
    total = 0.0
    a = namedtuple('a', ['name', 'price', 'shares'])
    for rec in records:
        s = a(*rec)
        total += s.shares * s.price
    return total

print(compute_cost2(records))
