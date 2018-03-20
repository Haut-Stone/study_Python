'''

'''

# 简单的用format函数即可

x = 1234.56789
print(format(x, '0.2f'))
print(format(x, '>10.1f'))
print(format(x, '<10.1f'))
print(format(x, '^10.1f'))
print(format(x, ','))  # 用逗号来分隔千位
print(format(x, '0,.1f'))
print(format(x, 'e'))
print(format(x, '0.2E'))

s = 'The value is {:0,.2f}'.format(x)
print(s)

print(format(x, '0.1f'))
print(format(-x, '0.1f'))

# 当然也可以用特殊的方式来交换， 和.
swap_separators = {ord('.'): ',', ord(','): '.'}
print(format(x, ',').translate(swap_separators))