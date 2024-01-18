# Class 36
"""
make your own your list,print the list in reverse.
"""
# lst = [100,25,14,15.5,'roshan',True,78,15]
#
# for i in range(len(lst)-1,-1,-1):
#     print(lst[i],end=' ')

"""
make your own list, print all even numbers
"""
# lst = [100,25,14,15.5,78,15,17,18,22,69,65,68,70]
#1. by index number
# for i in range(0,len(lst)):
#     if lst[i]%2==0:
#         print(lst[i],end=' ')

#2. by value directly

# for i in lst:
#     if i%2==0:
#         print(i,end=' ')

"""
make your own list, print all odd numbers
"""
# lst = [100,25,14,15.5,78,15,17,18,22,69,65,68,70]
#
# for i in lst:
#     if i%2 != 0:
#         print(i,end=' ')

"""
make your own list, print all element present at even index numbers
"""
# lst = [100,25,14,15.5,78,15,17,18,22,69,65,68,70]

# for i in range(0,len(lst)):
#     if i%2 == 0:
#         print(lst[i],end=' ')

"""
make your own list, print the sum of  all element present in given list
"""
# iterate by value

# lst = [100,25,14,15.5,78,15,17,18,22,69,65,68,70]
# total = 0
#
# for i in lst:
#     total = total + i
# print(total)

# iterate by index
# lst = [100,25,14,15.5,78,15,17,18,22,69,65,68,70]
#
# total = 0
#
# for i in range(0,len(lst)):
#     total = total + lst[i]
# print(total)

"""
make your own list, count the number of even numbers present in given list
"""
# lst = [100,25,14,15.5,78,15,17,18,22,69,65,68,70,10]
# count = 0
# for i in lst:
#     if i%2==0:
#         count = count + 1
# print(f'total noumber of even numbers is {count}')

"""
make your own list, count how many numbers are divisible by both 2 and 5
in given list
"""
# lst = [100,25,14,15.5,78,15,17,18,22,69,65,68,70,10]
# count = 0
# for i in lst:
#     if i%2==0 and i%5==0:
#         count = count+1
# print(f'total numbers are divisible by both 2 and 5 is:- {count}')

"""
make your own list, print the sum of  all even numbers present in given list
"""
# lst = [100,25,14,15.5,78,15,17,18,22,69,65,68,70,10]
#
# total = 0
#
# for i in lst:
#     if i%2 == 0:
#         total = total+i
# print(total)

"""
make your own list, print the largest number in given list
"""
lst = [100,25,14,15.5,780,15,17,180,22,69,65,68,70,108]

larg_num = lst[0]
sec_larg_num = lst[0]

for i in lst:
    if i>larg_num:
        larg_num = i
for i in lst:
    if i>sec_larg_num and i!=larg_num:
        sec_num = i
print(larg_num)
print(sec_larg_num)

"""
make your own list, print the smallest number in given list
"""
# lst = [100,25,14,15.5,780,15,17,1800,22,69,65,68,70,108]
#
# small_num = lst[0]
#
#
# for i in lst:
#     if i<small_num:
#         small_num = i
# print(small_num)