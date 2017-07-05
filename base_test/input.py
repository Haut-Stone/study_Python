# -*- coding: utf-8 -*-
# @Author: Haut-Stone
# @Date:   2017-07-04 21:33:50
# @Last Modified by:   Haut-Stone
# @Last Modified time: 2017-07-04 22:31:23

# 这里的因为有输入所以只能在命令行里面进行调试了
message = input("Tell me something , and I will repeat it back to you: ")
print(message)

# 处理输入的整数
height = input("How tall are you, in inches? ")
height = int(height)

if height > 36:
	print("\nYou're tall enough to ride!")
else:
	print("\nYou'll be able to ride when you're a little older!")

# 求模运算符	
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
	print("\nThe number " + str(number) + "is even.")
else:
	print("\nThe number " + str(number) + "is odd.")

# 使用用户输入来填充字典
responses = {}
polling_active = True

while polling_active:
	name = input("\nWhat is your name?")
	response = input("Which mountain would you like to climb someday?")
	responses[name] = response

	repeat = input("Would you like to let another person respond? (yes/no) ")
	if repeat == 'no':
		polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
	print(name + " would like to climb " + response + ".")