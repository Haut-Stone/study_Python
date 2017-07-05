# -*- coding: utf-8 -*-
# @Author: Haut-Stone
# @Date:   2017-07-04 13:39:47
# @Last Modified by:   Haut-Stone
# @Last Modified time: 2017-07-04 16:00:52

bicycles = ['trek', 'cannondale', 'redline','specialized']
print(bicycles)
# 测试的时候直接print也许是个不错的选择

for i in xrange(0,4):
	print(bicycles[i])

# 当不知道列表长度的时候，直接用负数就可以从后面开始访问
print(bicycles[-1].title())
print(bicycles[-2].title())
print(bicycles[-3].title())
print(bicycles[-4].title())

# 列表是动态的，可以增删改查
# 修改
motrocycles = ['honda','yamaha','suzuki']
print(motrocycles)
motrocycles[0] = 'ducati'
print(motrocycles)
motrocycles[0] = 'honda'

# 添加
motrocycles.append('ducati')
print(motrocycles)
motrocycles = []
motrocycles.append('honda')
motrocycles.append('yamaha')
motrocycles.append('suzuki')
print(motrocycles)

# 插入
motrocycles.insert(0, 'ducati')
print(motrocycles)

#删除
motrocycles = ['honda','yamaha','suzuki']
print(motrocycles)
del motrocycles[0]
print(motrocycles)

# 另一种删除的方式，同时还能保留所删除元素的值
motrocycles = ['honda','yamaha','suzuki']
print(motrocycles)
popped_motrocycle = motrocycles.pop()
print(motrocycles)
print(popped_motrocycle)

# 弹出任何位置的元素
motrocycles = ['honda','yamaha','suzuki']
print(motrocycles)
first_owned = motrocycles.pop(0)
print('The first motrocycle I owned was a ' + first_owned.title() + '.')

# 根据值删除元素,要注意，remove方法只能删除符合条件的第一个值
motrocycles = ['honda','yamaha','suzuki','ducati']
print(motrocycles)
motrocycles.remove('ducati')
print(motrocycles)

# 排序, 这时元数据已经被改变了。
cars = ['bmw','audi','toyota','subaru']
cars.sort()
print(cars)
cars.sort(reverse = True)
print(cars)

#排序，不改变原数据
cars = ['bmw','audi','toyota','subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print(sorted(cars, reverse = True))
print("\nHere is the original list again:")
print(cars)

#逆序
cars = ['bmw','audi','toyota','subaru']
cars.reverse()
print(cars)
print(len(cars))

# 创建数值列表, 左闭右开
numbers = list(range(1, 1000))
print(numbers)
print("\n")

# 高级形式的生成列表,列表解析
squares = [value**2 for value in range(1, 11)]
print(squares)

# 列表切片 其实就是选取一部分,相当于部分for循环
players = ['charles','martina','michael','florence','eli']
print(players[0:3])
print(players[:4])# 自动的话是从第一个开始
print(players[2:])# 或者是从最后一个结束
print(players[-3:])# 同样这里负数值也是被允许的

# 当然切片也是可以被遍历的
players = ['charles','martina','michael','florence','eli']
print("Here are the first three players on my team:")
for player in players[:3]:
	print(player.title())

# 复制列表
my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[1:2]
print(my_foods)
print(friend_foods)
my_foods.append('cannoli')
friend_foods.append('ice cream')
print(my_foods)
print(friend_foods)

# Warning ! 像相面这样直接赋值的话是不行的。相当于让两个指针指向了同一个地方
friend_foods = my_foods
print(my_foods)
print(friend_foods)
my_foods.append('onion')
print(my_foods)
print(friend_foods)

# tuple 常量列表
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

for dimension in dimensions:
	print(dimension)

# 元组的值无法修改，但是可以整体重新赋值
print("Origanal dimensions:")
for dimension in dimensions:
	print(dimension)
dimensions = (400, 400)
print("\nModified dimensions:")
for dimension in dimensions:
	print(dimension)