# # class Person:
# #     def __init__(self,name,city):
# #         self.name = name
# #         self.city = city
# #
# #     def show(self):
# #         print(self.name)
# #         print(self.city)
# #
# # class EMP(Person):
# #     def show1(self):
# #         print('This is EMP Class')
# #
# # obj = EMP('Roshan','Pune')
# # obj.show()
# # obj.show1()
# #***************************************************
#
# class Person:
#     '''constructor'''
#     def __init__(self,name):
#         self.name = name
#
#     # To get name
#     def getName(self):
#         return self.name
#
#     # To check if this person is an employee
#     def isEmployee(self):
#         return False
#
# class Employee(Person):
#     # Inherited or Subclass (Note Person in bracket)
#     def isEmployee(self):
#         return True
#
# obj = Person('Roshan')  # An Object of Person
# print(obj.getName(),obj.isEmployee())
# print('*'*25)
# obj1 = Employee('Roshan')   # An Object of Employee
# print(obj1.getName(),obj1.isEmployee())

class Person:
    def __init__(self,idnumber,name):
        self.idnumber = idnumber
        self.name = name

    def display(self):
        print(f'Id:- {self.idnumber}\nName:- {self.name}')

class Emp(Person):
    def __init__(self,idnumber,name,city,salary):
        self.city = city
        self.salary = salary
        Person.__init__(self,idnumber,name)

    def display1(self):
        super().display()
        print(self.city)
        print(self.salary)

class Details(Emp):
    def __init__(self,idnumber,name,city,salary,age,pincode,):
        self.age = age
        self.pincode = pincode
        Emp.__init__(self,idnumber,name,city,salary)


    def show(self):
        super().display1()
        print(self.age)
        print(self.pincode)

obj = Details(1012,'Roshan','Mumbai',75000,29,441209)
obj.show()
