# -*- coding: utf-8 -*-
# @Author: Haut-Stone
# @Date:   2017-07-05 12:32:20
# @Last Modified by:   Haut-Stone
# @Last Modified time: 2017-07-05 16:47:27

# 终于开始面向对象了嘛2333333

# 类的首字母要大写
class Dog():
	"""docstring for Dog"""
	def __init__(self, name, age):
		self.name = name
		self.age = age
	
	def sit(self):
		print(self.name.title() + " is now sitting.")

	def roll_over(self):
		print(self.name.title() + " rolled over!")
	
my_dog = Dog('while', 6)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog's age is " + str(my_dog.age) + ".")

# 调用方法
my_dog.sit()
my_dog.roll_over()

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

my_new_car = Car('audi', 'a8', '2017')
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
		
# 修改属性的值

# 直接修改
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# 通过方法修改属性的值
my_new_car.update_odometer(20)
my_new_car.read_odometer()

# 通过方法对属性的值进行递增
my_used_car = Car('subaru','outback','2013')
print("my used car is " + my_used_car.make.title() + '.')

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()

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

my_tesla = ElectricCar('tesla', 'model s', '2016')
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()


