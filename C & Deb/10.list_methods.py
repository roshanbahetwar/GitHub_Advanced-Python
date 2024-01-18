# class 42
'''
make a own list, and remove all duplicate elements from list
'''
# lst = [12,55,66,'Roshan','code',True,25,65,65,12,12.5,65,]
# new_lst = []
#
# for i in lst:
#     if i not in new_lst:
#         new_lst.append(i)
# print(new_lst)

"""
make a own list,then ask a number from user,
if number exits in that list,then print index or position
of that number otherwise print -1.
"""
# lst = [12,55,66,25,65,65,12,12.5,65,]

# num = int(input('enter a number:- '))
#
# if num in lst:
#     pos = lst.index(num)
#     print(f'position of {num} is {pos}')
# else:
#     print(-1)

"""
make a list with 1,20 numbers
"""
# lst = []
# # by for loop
# for i in range(1,21):
#     lst.append(i)
# print(lst)
#
# # by list comprehension
# new_lst = [i for i in range(1,21)]
# print(new_lst)
#
# odd_even = ['even' if i%2==0 else 'odd' for i in range(1,21)]
# print(odd_even)

# [2,4,6,8......30]

# even_lst = [i for i in range(1,31) if i%2==0]
# print(even_lst)

"""
ask from user
start = 3
end = 100
make a list which is divisible by 2 and 3
"""

# start = int(input('enter start num:- '))
# end = int(input('enter ending num:- '))
# lst = [i for i in range(start,end+1) if i%2==0 and i%3==0]
# print(lst)