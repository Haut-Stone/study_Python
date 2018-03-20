'''

'''

x = 1234
print(x)
print(bin(x))  # 2
print(oct(x))  # 8
print(hex(x))  # 16

# 如果不希望出现前缀，可以用format函数

print(format(x, 'b'))
print(format(x, 'o'))
print(format(x, 'x'))

x = -1234
print(format(x, 'b'))
print(format(x, 'x'))

print(format(2**23 + x, 'b'))
print(format(2**23 + x, 'x'))
print(int('4d2', 16))
print(int('10011010010', 2))