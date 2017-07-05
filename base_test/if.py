# -*- coding: utf-8 -*-
# @Author: Haut-Stone
# @Date:   2017-07-04 16:10:09
# @Last Modified by:   Haut-Stone
# @Last Modified time: 2017-07-04 20:29:22

# 一个简单的实例
cars = ['audi','bmw','subaru','toyota']

for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())

requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
	print("Hold the anchovies")

# 返回真假值
requested_topping = ['mushrooms','onions','pineapple']
print('mushrooms' in requested_topping)
print('pepproni' in requested_topping)

# 检查特定的值是否包含在列表中
banned_users = ['andrew','carolina','david']
user = 'marie'
if user not in banned_users:
	print("Oh no ! you are not in the list")

# if-else
age = 64

if age < 4:
	price = 0
elif age < 18:
	price = 5
elif age < 65:
	price = 10
else:
	price = 5;
print("Your admission cost is $" + str(price) + ".")

# 确定列表是不是空的
requested_toppings = []
if requested_toppings:
	for requested_topping in requested_toppings:
		print("Adding " + requested_topping + '.')
	print("\nFinished making your pizza")
else:
	print("Are you sure you want a plain pizza?")

# 使用多个列表
available_toppings = ['mushrooms','olives','green peppers','pepproni',
					  'pineapple','extra cheese']
requested_toppings = ['mushrooms','french fries','extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print("Adding " + requested_topping)
	else:
		print("Sorry, we don't have " + requested_topping + ".")


