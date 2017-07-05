# -*- coding: utf-8 -*-
# @Author: Haut-Stone
# @Date:   2017-07-05 20:59:44
# @Last Modified by:   Haut-Stone
# @Last Modified time: 2017-07-05 22:19:19

import unittest
from test_things import get_formatted_name
from test_things import AnonymousSurvey

# 手写测试函数的例子，当然以后都会变成自动化测试
# print("Enter 'q' at any time to exit the program.")
# while True:
# 	first = input("\nplease give me a first name:")
# 	if first == 'q':
# 		break
# 	last = input("please give me a lase name: ")
# 	if last == 'q':
# 		break

# 	formatted_name = get_formatted_name(first, last)
# 	print("\tNeatly formatted name: " + formatted_name + '.')

# 自动化测试一个函数
class NamesTestCase(unittest.TestCase):

	#注意这里的测试代码有py自己调用.
	def test_first_last_name(self):
		formatted_name = get_formatted_name('janis','joplin')
		self.assertEqual(formatted_name, 'Janis Joplin')

	def test_first_middle_last_name(self):
		formatted_name = get_formatted_name('wolfgang','mozart','amadeus')
		self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')


# 各种断言方法,解释我就不写了，显而易见
# assertNotEqual(a, b)
# assertEqual(a, b)
# assertTrue(x)
# assertFalse(x)
# assertIn(item, list)
# assertNotIn(item, list)


# 自动化测试一个类
class TestAnonmyousSurvey(unittest.TestCase):

	# 测试一个答案的情况
	def test_store_single_response(self):
		
		self.my_survey.store_response(self.responses[0])
		self.assertIn('English', self.my_survey.responses)

	# 测试3个答案的情况
	def test_store_three_response(self):

		for response in self.responses:
			self.my_survey.store_response(response)

		for response in self.responses:
			self.assertIn(response, self.my_survey.responses)

	# 提供测试数据的函数
	def setUp(self):

		question = "What language did you first learn to speak?"
		self.my_survey = AnonymousSurvey(question)
		self.responses = ['English','Spanish','Mandarin']

unittest.main()


