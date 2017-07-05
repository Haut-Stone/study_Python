# -*- coding: utf-8 -*-
# @Author: Haut-Stone
# @Date:   2017-07-04 20:29:51
# @Last Modified by:   Haut-Stone
# @Last Modified time: 2017-07-04 21:32:49

# 基本款
alien_0 = {'color':'green', 'points':5}
print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print("You have won " + str(new_points) + ". points!")

# 字典是一种动态的数据结构，可以修改其中的值
# 同样也具有增删改查的功能
# 增加
alien_0 = {'color':'green', 'points':5}
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# 修改
alien_0 = {'color':'green'}
print("The alien is " + alien_0['color'] + ".")
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")

alien_0 = {'x_position':0, 'y_position':25, 'speed':'medium'}
print("Original x-position is " + str(alien_0['x_position']))

if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print("now the x-position is " + str(alien_0['x_position']))

# 删除
alien_0 = {'color':'green', 'points':5}
print(alien_0)
del alien_0['points']
print(alien_0)

# 由类似对象组成的数组
favorite_languages = {
	'jen':'python',
	'sarah':'c',
	'edward':'ruby',
	'phil':'python',
}

print("Sarah's favorite language is " + favorite_languages['sarah'].title() + 
	  ".")

# 遍历字典
user_0 = {
	'username':'efermi',
	'first':'enrico',
	'last':'fermi',
}

for key, value in user_0.items():
	print('\nKey: ' + key)
	print('Value: ' + value) 

# 这里貌似按keys自动排序了
for name in favorite_languages.keys():
	print(name.title())
# 这里是手动排序,但是排序的标准不同
for name in sorted(favorite_languages.keys()):
	print(name.title() + ", thank you for taking the poll")

# 嵌套,看样子是用来代替结构体了呢
alien_0 = {'color':'green', 'points':5}
alien_1 = {'color':'yellow','points':10}
alien_2 = {'color':'red', 'points':15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
	print(alien)

# 程序自动填充外星人
aliens = []

for alien_number in range(30):
	new_alien = {'color':'green', 'points':5, 'speed':'slow'}
	aliens.append(new_alien)

for alien in aliens[:5]:
	print(alien)
print("......")

print("Total number of aliens is " + str(len(aliens)))

for alien in aliens[:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10

for alien in aliens[:5]:
	print(alien)
print("......")

print("Total number of aliens is " + str(len(aliens)))

# 字典中包含列表
favorite_languages = {
	'jen':['python','ruby'],
	'sarah':['c'],
	'edward':['ruby','go'],
	'phil':['python','haskell'],
}

for name, languages in favorite_languages.items():
	if len(languages) == 1:
		print("\n" + name.title() + "'s favorite language is:")
	else:
		print("\n" + name.title() + "'s favorite languages are:")
	for language in languages:
		print("\t" + language)

# 在字典中嵌套字典
users = {
	'aeinstein':{
		'first':'albert',
		'last':'einstein',
		'location':'princeton',
	},

	'mcurie':{
		'first':'marie',
		'last':'curie',
		'location':'pairs',
	},
}

for username, user_info in users.items():
	print("\nUsername: " + username)
	full_name = user_info['first'] + ' ' + user_info['last']
	location = user_info['location']

	print("\tFull name: " + full_name.title())
	print("\tLocation: " + location.title())
