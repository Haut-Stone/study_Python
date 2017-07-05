# -*- coding: utf-8 -*-
# @Author: Haut-Stone
# @Date:   2017-07-04 12:49:19
# @Last Modified by:   Haut-Stone
# @Last Modified time: 2017-07-04 15:42:40

name = 'jack lee'
name2 = 'JACK LEE'
# 将首字母变为大写,其余字母都变为小写，便于统一格式
# 同时这对于用户的非法输入是十分有用的处理方式，方便用统一的格式进行存储
print(name.title())
print(name.upper())
print(name2.title())
print(name2.lower())

first_name = "Jiahuan"
last_name = 'Shi'
full_name = first_name + ' ' + last_name
message = 'hello! ' + full_name + ' nice shoot!'
print(message)


# 特殊符号
print("\tPython")
print("Language:\n\tPython\n\tC\n\tJava")

# 删除末尾空白字符（无法显示字符包括\t \n） 
best_language = "Python "
print(best_language)
print(best_language.rstrip())# 这时原字符串并没有被改变
print(best_language)
best_language = best_language.rstrip()# 这时源字符串才被改变了
print(best_language)

# 按条件删除空格 可以见到删除空格的部位不一样
fa_language = "  Python  "
print(fa_language)
print(fa_language.lstrip())
print(fa_language.rstrip())
print(fa_language.strip())

# test
my_name = "ShiJiahuan"
print("hello " + my_name + ",would you like to learn some Python today?")

your_first_name = "katou"
your_last_name = "megumi"
your_full_name = your_first_name + ' ' + your_last_name

print(your_full_name.upper())
print(your_full_name.lower())
print(your_full_name.title())

print('Albert Einstein once said, "A person who never made a mistake never tried anything new."')

famous_people = 'Albert Einstein'
message = famous_people + ' once said, "A person who never made a mistake never tried anything new."'
print(message)

test = '  \n\twang wang   \t'
print(test)
print(test.lstrip())
print(test.rstrip())
print(test.strip())