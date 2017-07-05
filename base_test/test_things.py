# -*- coding: utf-8 -*-
# @Author: Haut-Stone
# @Date:   2017-07-05 21:31:05
# @Last Modified by:   Haut-Stone
# @Last Modified time: 2017-07-05 22:03:25

def get_formatted_name(first, last, middle = ''):
	if middle:
		full_name = first + ' ' + middle + ' ' + last
	else:
		full_name = first + ' ' + last
	return full_name.title()

class AnonymousSurvey():
	# 收集匿名调查问卷的答案
	
	def __init__(self, question):
		self.question = question
		self.responses = []

	def show_question(self):
		print(self.question)

	def store_response(self, new_response):
		self.responses.append(new_response)

	def show_responses(self):
		print("Survey result:")
		for response in responses:
			print('- ' + response)