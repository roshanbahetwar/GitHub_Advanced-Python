# Example of default constructor :
class Employee:
    def __init__(self):
        self.id = 'TM210'
        self.name = 'Roshan'
        self.city = 'Pune'

    def show(self):
        print('Id:-', self.id)
        print('Name:-', self.name)
        print('City:-', self.city)
emp = Employee()
emp.show()