# -*- coding: utf-8 -*-
# @Author: Haut-Stone
# @Date:   2017-07-05 16:55:00
# @Last Modified by:   Haut-Stone
# @Last Modified time: 2017-07-05 16:58:50

# car类
class Car(object):
	"""docstring for Car"""
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		long_name = str(self.year) + " " + self.make + " " + self.model
		return long_name.title()

	def read_odometer(self):
		print("This car has " + str(self.odometer_reading) + " miles on it.")

	def update_odometer(self, mileags):
		if mileags >= self.odometer_reading:
			self.odometer_reading = mileags
		else:
			print("You can't roll back an odometer!")

	def increment_odometer(self, miles):
		if miles >= 0:
			self.odometer_reading += miles
		else:
			print("You can't roll back an odometer!")

class Battery():
	def __init__(self, battery_size = 70):
		self.battery_size = battery_size

	def describe_battery(self):
		print("This car has a " + str(self.battery_size) + "-kMh battery.")

	def get_range(self):
		if self.battery_size == 70:
			rrange = 240
		elif self.battery_size == 85:
			rrange = 270
		message = "This car can go approximately " + str(rrange)
		message += " miles on a full charge"
		print(message)

# 继承(这里和书上写的有了些许的不同)， 这里貌似用了py2.7的写法
class ElectricCar(Car):

	def __init__(self, make, model, year):
		super(ElectricCar, self).__init__(make, model, year)
		self.battery = Battery()

	# 重写父类的方法,调用时会覆盖父类中的同名方法
	def fill_gas_tank():
		print("This car doesn't need a gas tank!")
