'''
考虑性能的话，要比匿名函数lambda更佳优秀
'''

from operator import itemgetter


rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'Jhon', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))

for p in rows_by_fname:
    print(p)
for p in rows_by_uid:
    print(p)

# itemgetter函数可以接受多个键

rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
print(rows_by_lfname)

# 当然这和用匿名函数的作用是一样的。

a = min(rows, key=itemgetter('fname'))
print(a)
