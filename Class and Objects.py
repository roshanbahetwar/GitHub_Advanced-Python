# # # class Dog:
# # # 	# simple class & attribute
# # # 	attr1 = 'mammal'
# # # 	attr2 = 'dog'
# # #
# # # 	def fun(self):
# # # 		# A sample method
# # # 		print('This is animal',self.attr1)
# # # 		print('This is animal',self.attr2)
# # #
# # # obj = Dog()
# # # obj.fun()
# # # print(obj.attr1)
# #
# # # it is clearly seen that self and obj is referring to the same object
# # # class Check:
# # # 	def __init__(self):
# # # 		"""it is clearly seen that self and obj is
# # # 			 referring to the same object"""
# # # 		print('Address of self:- ',id(self))		# id of self and obj is same
# # #
# # # obj = Check()
# # # print('Address of obj:- ',id(obj))
# #
# # class Car:
# # 	def __init__(self,model,color):
# # 		self.model = model
# # 		self.color = color
# #
# # 	def show(self):
# # 		print('*' * 50)
# # 		print('the model is:- ',self.model)
# # 		print('the model color is:= ',self.color)
# # 		print('*' * 50)
# #
# # audi = Car('Audi_x45','Red')
# # ferrari = Car('Ferrari_fx465','Blue')
# # audi.show()
# # ferrari.show()
#
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


# Sample class with init method
class Person:
	def __init__(self,name):
		self.name = name

	def show(self):
		print('My name is:- ',self.name)

obj = Person('Roshan')
obj.show()