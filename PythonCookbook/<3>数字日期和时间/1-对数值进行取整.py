'''

'''

print(round(1.23, 1))
print(round(1.27, 1))
print(round(-1.27, 1))
print(round(1.25361, 3))

# 需要注意的是，当某个值恰好等于两个整数间的一半时，会取整到最接近的那个偶数上。
# 比如1.5，2.5都会取到2上。

a = 1627731
print(round(a, -1))  # 负数则取整到十位上
print(round(a, -2))
print(round(a, -3))

# 但是只是输出的话，不用round，用format就可以了
x = 1.23456
print(format(x, '0.2f'))
print(format(x, '0.3f'))
print('value is {:0.3f}'.format(x))

# 另外不建议用round来修复精度问题，建议用decimal模块

a = 2.1
b = 4.2
c = a + b
print(c)
c = round(c, 2)  # Noooo! Don't do this!
print(c)