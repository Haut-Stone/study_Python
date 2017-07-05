# -*- coding: utf-8 -*-
# @Author: Haut-Stone
# @Date:   2017-07-04 22:32:13
# @Last Modified by:   Haut-Stone
# @Last Modified time: 2017-07-05 12:28:28
import pizza

# 用这种导入方法的话，下面调用的时候不需要加模块的名字
# from pizza import out_make_pizza

def greet_user():
	"""显示简单的问候语"""
	print("hello!")

# 不调用的话是不会显示的
greet_user()

# 这里貌似是同名函数会自动覆盖
def greet_user(username):
	print("Hello " + username.title() + "!")

greet_user('Shi Jiahuan')

# 传递实参
def describe_pet(animal_type, pet_name):
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster','harry')

# 关键字实参,可以无视位置顺序
describe_pet(animal_type = 'hamster', pet_name = 'harry')

# 默认值
def describe_pet(pet_name,animal_type = 'dog'):
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name = 'harry')

# 返回简单值
def get_formatted_name(first_name, last_name):
	full_name = first_name + " " + last_name
	return full_name.title()
musican = get_formatted_name('jimi','hendrix')
print(musican)

# 让实参变的可以被选择
def get_formatted_name(first_name, last_name, middle_name = ''):
	if middle_name:
		full_name = first_name + ' ' + middle_name + ' ' + last_name
	else:
		full_name = first_name + ' ' + last_name
	return full_name.title()

musican = get_formatted_name('jimi','hendrix')
print(musican)

musican = get_formatted_name('john','hooker','lee')
print(musican)

# 返回字典, 这是一个很好用的特性
def build_person(first_name, last_name):
	person = {'first':first_name,'last':last_name}
	return person
musican = build_person('jimi','hendrix')
print(musican)

# 传递列表,当然这里的列表元数据直接就被修改了
def greet_users(names):
	for name in names:
		msg = "Hello, " + name.title() + "!"
		print(msg)
usernames = ['ShiJiahuan','WangShaoyu','ZhangFan']
greet_users(usernames)

# 禁止函数修改列表,可以通过切片的方式传递副本
# 例如function_name(list_name[:])

# 传递任意数量的实参
def make_pizza(*toppings):
	print(toppings)

make_pizza('pepperoni')
make_pizza('mushroom','green peppers','extra cheese')

# 结合使用任意位置实参和任意数量实参
def make_pizza(size, *toppings):
	print("\nMaking a " + str(size) + "-inch pizza with the follow toppings:")
	for topping in toppings:
		print("- " + topping)

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushroom','green pepper','extra cheese')

# 使用任意数量的关键字实参
def build_profile(first, last, **user_info):
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile

user_profile = build_profile('albert','einstein',location = 'princetion',field =
							 'physics')
print(user_profile)

pizza.out_make_pizza(20, 'pepperoni')
pizza.out_make_pizza(12, 'mushroom','green peppers','extra cheese')

