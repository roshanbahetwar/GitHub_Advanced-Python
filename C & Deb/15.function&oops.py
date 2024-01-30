# Day:3
class Students:
    # Method
    def __init__(self): # initializer
        self.name = input('enter name: ')
        self.age = int(input('enter age: '))
        self.city = input('enter city: ')

    def show(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'City: {self.city}')

obj1 = Students()
obj1.show()
print('*'*25)
obj2 = Students()
obj2.show()
