"""
ask 2 numbers from user
and print which number is greatest
"""

# num1 = int(input("enter num1 = "))
# num2 = int(input("enter num2 = "))
#
# if num1>num2:
#     print(f'{num1 = } is greatest.')
# elif num1<num2:
#     print(f'{num2 = } is greatest.')
# else:
#     print(f'both are equal.')
#
# print('Thanks for Asking...')

"""
ask numbers from user
and print if the number is odd or even
"""

# num=int(input("enter num = "))
#
# if num%2==0:
#     print(f'{num} is even.')
# else:
#     print(f'{num} is odd.')

"""
ask from users physics and chemistry marks
print Pass if students pass in both subjects
"""
# physics = int(input("enter your physics subject marks= "))
# chemistry = int(input("enter your chemistry subject marks= "))
#
# if physics>=33 and chemistry>=33:
#     print('Pass')
# else:
#     print('Fail')

"""
write python programs that takes an integer input and
print whether it is positive integer or negative integer
(consider 0 is positive)
"""

# num= float(input("enter the number= "))
# if num>=0:
#     print(f'{num} is positive number.')
# else:
#     print(f'{num} is negative number.')

"""
write a program that take a character as input
and print whether it is Vowel or consonant.
"""
# char= input("enter charactor= ")
#
# if char.lower() in ("a","e","i",'o',"u"):
#     print(f'{char} is vowel')
# else:
#     print(f'{char} is consonant')

"""
write a program thats take two number as input
and check fisrt number is divisible by the second.
"""
# num1 = int(input('enter the num1= '))
# num2 = int(input('enter the num2= '))
#
# if num1%num2==0:
#     print(f'Yes, {num1} is divisible by {num2}.')
# else:
#     print(f'No, {num1} is not divisible by {num2}.')

"""
a student will not allowed to sit in her/his exam
if attendance is less than 75%, find attendance in percentage
and he/she allowed or not in exam?
"""

total_class = int(input("enter the total class held= "))
total_class_attend = int(input("total class attend= "))
per_attendance = float((total_class_attend/total_class)*100)

print(f'Percentage of Class attend {round(per_attendance,2)}%')
if per_attendance>=75:
    print("please allow to sit in exam")
else:
    print("not allowed to sit in exam.")