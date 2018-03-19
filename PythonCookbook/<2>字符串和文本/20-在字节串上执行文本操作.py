'''

'''
import re

data = b'Hello World'
print(data[0:5])
print(data.startswith(b'Hello'))
print(data.split())
print(data.replace(b'Hello', b'Hello Cruel'))

# 类似的操作在字节数组上也能完成

data = bytearray(b'Hello World')
print(data[0:5])

# 同样re也可以用在字节串上

data = b'FOO:BAR,SAMP'
print(re.split(b'[:,]', data))

# 但是有的操作还是有一点区别的

a = "Hello World"
print(a[0])
print(a[1])
b = b'Hello World'
print(b[0])
print(b[1])

s = b'Hello World'
print(s)  # 多了字节串的前缀
print(s.decode('ascii'))  # 消除了字节串的前缀

# 另外在字节串上，无法尽行format操作
