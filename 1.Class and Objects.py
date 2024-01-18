### Sources from Geeks for Geeks ##

# class Dog:
# 	# simple class & attribute
# 	attr1 = 'mammal'
# 	attr2 = 'dog'
#
# 	def fun(self):
# 		# A sample method
# 		print('This is animal',self.attr1)
# 		print('This is animal',self.attr2)
#
# obj = Dog()
# obj.fun()
# print(obj.attr1)
#****************************************************
# class Check:
# 	def __init__(self):
# 		"""it is clearly seen that self and obj is
# 			 referring to the same object"""
# 		print('Address of self:- ',id(self))		# id of self and obj is same
#
# obj = Check()
# print('Address of obj:- ',id(obj))
#****************************************
# class Car:
# 	def __init__(self,model,color):
# 		self.model = model
# 		self.color = color
#
# 	def show(self):
# 		print('*' * 50)
# 		print('the model is:- ',self.model)
# 		print('the model color is:= ',self.color)
# 		print('*' * 50)
#
# audi = Car('Audi_x45','Red')
# ferrari = Car('Ferrari_fx465','Blue')
# audi.show()
# ferrari.show()

# *************************************************
# class ABC:
# 	def __init__(self,name,company):
# 		self.name = name
# 		self.company = company
#
# 	def show(self):
# 		print('My name is '+ self.name +' '+  'and i am work in '+ self.company)
#
# obj = ABC('Roshan','TechMahindra')
# obj.show()
#************************************************
#  Sample class with init method
# class Person:
# 	def __init__(self,name):
# 		self.name = name
#
# 	def show(self):
# 		print('My name is:- ',self.name)
#
# obj = Person('Roshan')
# obj.show()
#*************************************************************
# class Person:
# 	def __init__(self,name,company):
# 		self.name = name
# 		self.company = company
#
# 	def __str__(self):
# 		return f'My Name is {self.name} and i work in {self.company}'
#
# obj = Person('Roshan','TechMahindra')
# print(obj)
#
# obj = Person('Ajay','IndianRalway')
# print(obj)
#*************************************************************

# class Dog:
# 	# class variable
# 	animal = 'dog'     					# class variable
# 	def __init__(self,breed,color):     # instance variable
# 		self.breed = breed
# 		self.color = color
#
# 	def show(self):
# 		print('Breed: ',self.breed)
# 		print('Color: ',self.color)
#
#
# Rodger = Dog('Pug','Brown')
# print('Rodger Details: ')
# print('Rodger is',Dog.animal)
# Rodger.show()
# print('*'*20)
#
# Buzo = Dog('Bulldog','Black')
# print('Buzo Details: ')
# print('Buzo is',Dog.animal)
# Buzo.show()
# print('*'*20)
#
# Xylo = Dog('X-Dog','White')
# print('Xylo Details:- ')
# print('Xylo is',Dog.animal)
# Xylo.show()
#*********************************************

# class Dog:
# 	animal = 'dog'
#
# 	def __init__(self,breed):
# 		self.breed = breed
#
# 	def setColor(self,color):
# 		self.color = color
# 	def getColor(self):
# 		return self.color
#
# obj = Dog('pug')
# obj.setColor('White')
# col = obj.getColor()
# print(col)