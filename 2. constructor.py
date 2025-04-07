# Example of default constructor : No any arguments instead of self
# class Employee:
#     def __init__(self):
#         self.id = 'TM210'
#         self.name = 'abc'
#         self.city = 'Pune'
#
#     def show(self):
#         print('Id:-', self.id)
#         print('Name:-', self.name)
#         print('City:-', self.city)
# emp = Employee()
# emp.show()
#*****************************************

# Example of the parameterized constructor :
# class Addition:
#     # first = 0
#     # second = 0
#     # answer = 0
#
#     def __init__(self,first,second):
#         self.first = first
#         self.second = second
#
#
#     def show(self):
#         print('First Number: ',self.first)
#         print('Second Number: ',self.second)
#         print('Addition of Two Number: ',self.answer)
#
#     def calculate(self):
#         self.answer= self.first + self.second
#         return self.answer
#
# obj = Addition(10,35)
# obj.calculate()
# obj.show()
# print('*'*35)
#
# obj1 = Addition(1500,354)
# obj1.calculate()
# obj1.show()
#**************************************************
# class MyClass:
#     def __init__(self, name = None):
#         if name is None:
#             print('Default constructor called')
#         else:
#             self.name = name
#             print('Parameterized constructor called',self.name)
#
#     def method(self):
#         if hasattr(self,'name'):
#             print('Method call with name',self.name)
#         else:
#             print('method call without name')
#
# obj = MyClass()
# obj.method()
# print('*'*20)
# obj2 = MyClass('abc')
# obj2.method()
# print('*'*25)
#******************************************************

### Destructor ###
class Emp:
    def __init__(self):
        print('employee created...')

    def __del__(self):
        print('Destructor called, employee deleted')
obj_d = Emp()
del obj_d

class Employee:
    # Initializing
    def __init__(self):
        print('Employee Created')

    # calling destructor
    def __del__(self):
        print('Destructor called')
def create_obj():
    print('making object..')
    obj = Employee()
    print('function end')
    return obj

print('calling create obj() function...')
obj = create_obj()
print('program end...')

""" Above Example: This example gives the explanation of above-mentioned note. 
Here, notice that the destructor is called after the ‘Program End…’ printed."""

