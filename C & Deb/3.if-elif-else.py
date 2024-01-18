# class -19 & 20
"""
write program that takes multiple subjects marks as input
and calculate percentage and their grade as per percentage
"""
# physics = int(input("enter the physics marks = "))
# maths = int(input("enter the maths marks = "))
# som = int(input("enter the som marks = "))
# tom = int(input("enter the tom marks = "))
# kom = int(input("enter the kom marks = "))
#
# total_marks = physics+maths+som+tom+kom
# percentage = (total_marks/500)*100
# print(f'Percentage {percentage:.2f}%')
#
# if percentage>=91 and percentage<=100:
#     print("A Grade")
# elif percentage>=81 and percentage<=90:
#     print('B Grade')
# elif percentage>=71 and percentage<=80:
#     print('C Grade')
# elif percentage>=61 and percentage<=70:
#     print('D Grade')
# elif percentage>=1 and percentage<=60:
#     print('Fail')
# else:
#     print('invalid percentage')

"""
write program to check number is odd,even or equal to zero
"""
# num = int(input("enter the number = "))
#
# if num ==0:
#     print("it is equal to zero")
# elif num%2==0:
#     print("even number")
# else:
#     print("odd number")

"""
write python code.
"""

# num = list(range(0,20))
# two_lst = []
# eight_lst = []
# three_lst = []
# other_lst = []
#
# for i in num:
#     if i%2==0 and i%8!=0:
#         two_lst.append(i)
#     elif i%8==0:
#         eight_lst.append(i)
#     elif i%3==0:
#         three_lst.append(i)
#     else:
#         other_lst.append(i)
#
# print(two_lst)
# print(eight_lst)
# print(three_lst)
# print(other_lst)

"""
write a python code thats check a number,whether it is divisible by 2 and 3 but not 8 
"""

# num = int(input("enter the number= "))
#
# if num%2==0 and num%3==0 and num%8!=0:
#     print("yes,it is divisible by 2 and 3,but not 8")
# else:
#     print('no')

"""
write a program to print the last digit of given number, and check last digit is divisble by 5 or not
"""
# num = int(input("enter the number= "))
#
# last_digit = num%10
# print(f'last digit of {num} is : {last_digit}')
#
# if last_digit%5==0:
#     print("it is divisible by 5")
# else:
#     print("not divisible by 5")

"""
write python program for given condion, calculate final bill with discount
"""

# bill_amount = float(input("enter the total bill= "))
#
# if bill_amount>=50000:
#     discount = 30
# elif bill_amount>=40000 and bill_amount<50000:
#     discount = 25
# elif bill_amount>=30000 and bill_amount<40000:
#     discount = 20
# elif bill_amount>=10000 and bill_amount<30000:
#     discount = 10
# else:
#    discount = 0
#
# print(f'you got {discount}% discount')
# final_bill = bill_amount-(bill_amount*30/100)
# print(f'your final bill is {final_bill} Rs')

"""
write a program to take four number from users,ensure all numbers are different
and print which number is smallest
"""

num1 = int(input('enter num1= '))
num2 = int(input("enter num2= "))
num3 = int(input("enter num3= "))
num4 = int(input("enter num4= "))

if num1<num2 and num1<num3 and num1<num4:
    print(f'num1= {num1} is smallest')
elif num2<num1 and num2<num3 and num2<num4:
    print(f'num2= {num2} is smallest')
elif num3<num1 and num3<num2 and num3<num4:
    print(f'num3= {num3} is smallest')
else:
    print(f'num4= {num4} is smallest')