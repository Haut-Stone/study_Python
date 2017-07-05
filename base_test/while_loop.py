# -*- coding: utf-8 -*-
# @Author: Haut-Stone
# @Date:   2017-07-04 21:55:42
# @Last Modified by:   Haut-Stone
# @Last Modified time: 2017-07-04 22:24:45

# while循环
current_number = 1
while current_number <= 5:
	print(current_number)
	current_number += 1

prompt = "\nTell me something, and I will back it to you: "
prompt += "\nEnter 'quit' to end this program\n"

# 这里有2种不同的方式以供参考
# message = ""
# while message != 'quit':
# 	message = input(prompt)
# 	if message != 'quit':
# 		print(message)

# active  = True
# while active:
# 	message = input(prompt)

# 	if message == 'quit':
# 		active = False
# 	else:
# 		print(message)

# prompt = "\nPlease enter the name of a city you have vistied:"
# prompt += "\n(Enter 'quit' when you are finished)"

# while True:
# 	city = input(prompt)
# 	if city == 'quit':
# 		break
# 	else:
# 		print("I'd love to go to " + city.title() + "!")

# 在循环中使用continue
current_number = 0
while current_number < 10:
	current_number += 1
	if current_number % 2 == 0:
		continue
	print(current_number)

# 在列表之间移动元素
unconfimed_users = ['alice','brian','candace']
confirmed_users = []

while unconfimed_users:
	current_user = unconfimed_users.pop()
	print("Verifying user: " + current_user.title())
	confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
	print(confirmed_user.title())

