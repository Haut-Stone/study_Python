# -*- coding: utf-8 -*-
# @Author: Haut-Stone
# @Date:   2017-07-05 17:08:38
# @Last Modified by:   Haut-Stone
# @Last Modified time: 2017-07-05 17:52:50

# 打开txt文件
with open('pi_digits.txt') as file_object:
	contents = file_object.read()
	print(contents)


# 逐行读取
filename = 'pi_digits.txt'

with open(filename) as file_object:
	for line in file_object:
		print(line.rstrip())


# 创建一个包含文件各行内容的列表
filename = 'pi_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

for line in lines:
	print(line.rstrip())


# 使用文件内容
filename = 'pi_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

pi_string = ''
for line in lines:
	pi_string += line.strip()

print(pi_string)
print(len(pi_string))

# 写入空文件
filename = "programing.txt"

with open(filename, 'w') as file_object:
	file_object.write("I love megumi!\n")

# 附加到文件
filename = "programing.txt"
with open(filename, 'a') as file_object:
	file_object.write("I also love finding meaning in large datasets.\n")
	file_object.write("I love creating apps that can run in a browser.\n")