# -*- coding: utf-8 -*-
# @Author: Haut-Stone
# @Date:   2017-07-04 14:37:39
# @Last Modified by:   Haut-Stone
# @Last Modified time: 2017-07-04 14:54:25

# 基本款
magicians = ['alice','david','carolina']
for magician in magicians:
	print(magician)

# 一般款
magicians = ['alice','david','carolina']
for magician in magicians:
	print(magician.title() + ', that was a great trick!')
	print("I can't wait to see your next trick, " + magician.title() + '.\n')
print("Thank you, everyone. That was a magic show!")

# 数值范围内的循环
for value in range(1, 5):
	print(value)

# 创建数值列表, 左闭右开
numbers = list(range(1, 1000))
print(numbers)
print("\n")

# 多步创建数值列表
numbers = list(range(1, 1000, 5))
print(numbers)

# 循环中先列表加入元素
squares = []
for value in range(1, 100):
	square = value ** 2
	squares.append(square)
print(squares)