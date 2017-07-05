# -*- coding: utf-8 -*-
# @Author: Haut-Stone
# @Date:   2017-07-05 18:21:08
# @Last Modified by:   Haut-Stone
# @Last Modified time: 2017-07-05 20:59:34

import json

# 读写json文件
numbers = [2,3,5,7,11,13]

filename = 'numbers.json'
with open(filename, 'w') as f_obj:
	json.dump(numbers, f_obj)

tests = []
filename = 'numbers.json'
with open(filename, 'r') as f_obj:
	tests = json.load(f_obj)

print(tests)

# test
def greet_user():
	filename = 'username.json'
	try:
		with open(filename) as f_obj:
			username = json.load(f_obj)
	except IOError:
		username = input("What is yor name? ")
		with open(filename, 'w') as f_obj:
			json.dump(username, f_obj)
			print("We'll remember you when you come back, " + username + "!")
	else:
		print("Welcome back, " + username + "!")

greet_user()


