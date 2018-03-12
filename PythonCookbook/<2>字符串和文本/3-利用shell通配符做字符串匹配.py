'''
在python中用常用的shell通配符
'''

from fnmatch import fnmatch, fnmatchcase


print(fnmatch('foo.txt', '*.txt'))
print(fnmatch('foo.txt', '?oo.txt'))
print(fnmatch('dot45.csv', 'dot[0-9]*.csv'))
names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
print([name for name in names if fnmatch(name, 'Dat[0-9]*')])


# 但是注意，这里的大小写模式和底层操作系统有关

print(fnmatch('foo.txt', '*.TXT'))  # 但是在win上就是True

# 为了消除这种歧义，用fnmatchcase只认大小写，和系统无关

print(fnmatch('foo.txr', '*.TXT'))
