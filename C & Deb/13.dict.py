# class 55 to 57
# my_dict = {"name":"Roshan","age":25,"gender":"Male",}
# k = input('enter a key: ')
# result = my_dict.get(k)
#
# if result is not None:
#     print(result)
# else:
#     print("key does not exist.")
#***********************************************************
"""
ask a subject name and marks from user and add to dict
"""
# my_dict = {}
# while True:
#     subjects = input('enter a subject name: ')
#     marks = int(input('enter subjects marks out of 100: '))
#     my_dict[subjects] = marks
#
#     choice = input("Do you want to add more, [yes/no]: \n")
#
#     if choice.lower() == 'yes':
#         continue
#     else:
#         break
# print(my_dict)
#***********************************************************
# marks = {}
# sub_count = int(input('enter how many subjects = '))
# for _ in range(0,sub_count):
#     subj_name = input("enter subject name = ")
#     sub_marks = int(input(f"enter {subj_name} marks = "))
#     marks[subj_name] = sub_marks
# print(marks)
#***********************************************************
"""
convert two list into dict,same length of list
"""

# ls1 = ["math","hindi","english"]
# marks = [65,55,78]
#
# my_dict = dict(zip(ls1,marks))
# print(my_dict)
#***********************************************************
"""
convert two list into dict,same length of list
"""
# ls1 = ["math","hindi","english"]
# marks = [65,55,78]
#
# result = {}
#
# for i in range(len(ls1)):
#     result[ls1[i]] = marks[i]
# print(result)
#***********************************************************
"""
write a program to sum of all the items in a dict
"""
# my_dict = {
#     "math":65,
#     'english':78,
#     'history':65,
#     'science':77,
#     'computer':98
# }
#
# total = 0
# for v in my_dict.values():
#     total += v
# print(f"total subjects marks: {total}")

#***********************************************************
"""
write a program to multiply of all the items in a dict
"""
# my_dict = {
#     "math":65,
#     'english':78,
#     'history':65,
#     'science':77,
#     'computer':98
# }
#
# total = 1
# for v in my_dict.values():
#     total *= v
# print(f"multiply of all subjects marks: {total}")
#***********************************************************
"""
ask a string from user and print the each char with occurance
"""
# my_dict = {}
# userInput = input("enter a string: ")
# for char in userInput:
#     if char in my_dict:
#         my_dict[char] += 1
#     else:
#         my_dict[char] = 1
# print(my_dict)

# students_marks = {
#     'Roshan':[78,68,95,80,79],
#     'Mohan':[68,88,35,50,97],
#     'Ganesh':[81,65,45,41,48],
#     'Komal':[70,76,45,55,65]
# }
# for name,marks in students_marks.items():
#     total = sum(marks)
#     percentage = total/500*100
#     print(f"{name} has scored total marks {total}, percentage {percentage:.2f}")
# *********************************************************************************
# by using for loop instead of sum
# students_marks = {
#     'Roshan':[78,68,95,80,79],
#     'Mohan':[68,88,35,50,97],
#     'Ganesh':[81,65,45,41,48],
#     'Komal':[70,76,45,55,65]
# }
#
# for name,marks in students_marks.items():
#     total = 0
#     for mark in marks:
#         total += mark
#     percentage = total/500*100
#     print(f'{name} has scored total marks {total} and percentage: {percentage:.2f}')

# sub_marks_dict = {
#     'math':95,
#     'english':65,
#     'science':85,
#     'history':67,
#     'hindi':75,
# }
# sub_name = input("enter subject name: ").lower()
#
# if sub_name in sub_marks_dict:
#     print(f"the marks of {sub_name} subject is {sub_marks_dict[sub_name]}")
# else:
#     print('Invalid')
#**********************************************************************
# method 1

# students_marks = {
#     'Roshan':[78,68,95,80,79],
#     'Mohan':[98,88,75,50,97],
#     'Ganesh':[81,65,45,41,48],
#     'Komal':[70,76,45,55,65]
# }
#
# highest_marks = 0
# highest_marks_name = ''
# for name,marks in students_marks.items():
#     total = 0
#     for m in marks:
#         total += m
#         if total>highest_marks:
#             highest_marks = total
#             highest_marks_name = name
# print(f"{highest_marks} is the highest marks of {highest_marks_name}")

#******************
# method-2
# students_marks = {
#     'Roshan':[78,68,95,80,79],
#     'Mohan':[98,88,75,50,97],
#     'Ganesh':[81,65,45,41,48],
#     'Komal':[70,76,45,55,65]
# }
#
# highest_marks = 0
# highest_marks_name = ''
# for name,marks in students_marks.items():
#     total = sum(marks)
#     if total>highest_marks:
#         highest_marks = total
#         highest_marks_name = name
# print(f"{highest_marks} is the highest marks of {highest_marks_name}")
#************************************
# d1 = {"a":100,"b":200,"c":300,"d":150}
# d2 = {"a":300,"b":200,"c":130,"e":500}
#
# result = {}
#
# for k,v in d1.items():
#         result[k] = v
#
# for k,v in d2.items():
#     if k in result:
#         result[k] = result[k]+v
#     else:
#         result[k] = v
#
# print(result)
#*******************************************************************
# method-1, by using for loop
# students_data = {
#     'Roshan':{
#         'roll_no':11,
#         'gender':'Male',
#         'marks':[75,74,69,81]
#     },
#     'Mohan':{
#         'roll_no':12,
#         'gender':'Male',
#         'marks':[65,68,75,79],
#     },
#     'Ashs':{
#         'roll_no':13,
#         'gender':'Female',
#         'marks':[85,75,85,65],
#     }
# }
#
# for name,details in students_data.items():
#     total = 0
#     for mark in details['marks']:
#         total += mark
#     print(f"{name} got total {total} marks")
#***************************************************
# method-2,by using sum
# students_data = {
#     'Roshan':{
#         'roll_no':11,
#         'gender':'Male',
#         'marks':[75,74,69,81]
#     },
#     'Mohan':{
#         'roll_no':12,
#         'gender':'Male',
#         'marks':[65,68,75,79],
#     },
#     'Ashs':{
#         'roll_no':13,
#         'gender':'Female',
#         'marks':[85,75,85,65],
#     }
# }
#
# for name,details in students_data.items():
#     total = sum(details['marks'])
#     print(f"{name} got total {total} marks")
