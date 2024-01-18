# class 25 to 26
# for loop

"""
write program that print number from 1 to 10 by using for loop
"""
# for i in range(1,11):
#     print(i,end=' ')

"""
ask number from user and print that all numbers from 1 to user input
"""
# num = int(input('enter a number:- '))
# for i in range(1,num+1):
#     print(i,end=' ')

"""
ask number from user as N and print all numbers from N to 1
"""
# N = int(input('enter a number:- '))
# for i in range(N,0,-1):
#     print(i,end=' ')

"""
ask start and end numbers from user and print all numbers from start to end using for loop
"""
# start = int(input('enter a start number:- '))
# end = int(input('enter a end number:- '))

# for i in range(start,end+1):
#     print(i,end=' ')

"""
calculate the sum of all numbers from 1 to 10,
by using for loop.
"""
# sum = 0
# for i in range(1,11):
#     sum = sum+i
# print(sum)

"""
calculate the product of all numbers from 1 to 10,
by using for loop
"""
# prod = 1
# for i in range(1,11):
#     prod = prod*i
# print(prod)

"""
calculate how many numbers are divisible by 7 from 1 to 100,
by using for loop
"""
# count = 0
# for i in range(1,101):
#     if i%7==0:
#         count = count+1
# print(count)

"""
calculate how many numbers are divisible by 6 and 7 from 1 to 200,
by using for loop
"""
# count = 0
# for i in range(1,201):
#     if i%6==0 and i%7==0:
#         count = count+1
# print(count)

"""
write a program to calculate the sum of all the numbers divisible by 4
from 20 to 50 by using for loop.
"""
# total = 0
# for i in range(20,51):
#     if i%4==0:
#         total = total+i
# print(total)

"""
ask a number from user, and print the multiplication table of 
that number by using for loop.
"""
num = int(input('enter a number:- '))

for i in range(1,11):
    n = num*i
    print(f'{num}*{i}= {n}')