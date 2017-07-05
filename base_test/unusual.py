# -*- coding: utf-8 -*-
# @Author: Haut-Stone
# @Date:   2017-07-05 17:54:51
# @Last Modified by:   Haut-Stone
# @Last Modified time: 2017-07-05 18:20:38

# 异常
try:
	ans = 5/0
except ZeroDivisionError:
	print("You can't divide by zero!")
else:
	print(ans)

# 处理找不到文件的异常, 这里貌似py把类的名字也给改了
filename = 'alice.txt'

try:
	with open(filename) as f_obj:
		contents = f_obj.read()
except IOError:
	msg = "Sorry, the file " + filename + " does not exit."
	print(msg)

# 使用多个文件
def count_words(filename):
	try:
		with open(filename) as f_obj:
			contents = f_obj.read()
	except IOError:
		# pass 可用于什么都不提示的时候，充当占位符
		msg = "Sorry, the file " + filename + " doesn't exit."
		print(msg)
	else:
		words = contents.split()
		num_words = len(words)
		print("The file " + filename + "has about " + str(num_words) + " words."
			  )

filename = 'alice.txt'
count_words(filename)