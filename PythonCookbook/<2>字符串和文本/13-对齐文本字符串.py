'''

'''


text = 'Hello World'
print(text.rjust(20))
print(text.center(20))  # 左右都填充，总长度20

# 当然你也可以指定用什么东西来填充

print(text.rjust(20, "="))
print(text.center(20, "*"))

# 你也可以用format函数来完成这个任务

print(format(text, '>20'))
print(format(text, '=<20'))
print(format(text, '^20'))
print("{:>10} {:>10}".format('Hello', 'World'))

# format不仅对于字符串，而可以作用于任何值

x = 1.2345
print(format(x, '>10'))

# 在老代码中我们会用 % 等等，这不是我常用的吗= =
# 以后还是尽量用format把
