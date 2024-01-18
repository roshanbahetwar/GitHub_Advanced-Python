# class 38 to 40
"""
write a program that prompt the user to specify length of list
and then request numbers to populate that list. display the final list as
output.
"""
# list_len = int(input('enter list len:- '))
# result = []
#
# for i in range(0,list_len):
#     num = int(input('enter a number:- '))
#     result.append(num)
# print(result)

"""
Create a list and prompt(ask) the user for an 'old number and 
'new number.' If the 'old number' which exists in the list, replace it with the 
'new number' provided by the user.
"""
# my_lst = [22,21,55,63,25,85,66,35,41,21,21,23]
# print(my_lst)
#
# old_num = int(input('enter a old number:- '))
# new_num = int(input('enter a new number:- '))
#
# for i in range(0,len(my_lst)):
#     if my_lst[i] == old_num:
#         my_lst[i] = new_num
# print(my_lst)

"""
remove all even numbers from list
"""
#1.by using another list
# my_lst = [22,21,55,63,25,85,66,35,41,21,21,23]
#
# result = []
# for i in my_lst:
#     if i%2!=0:
#         result.append(i)
# print(result)

##2.by using remove method
# my_lst = [22,21,55,63,25,85,66,35,41,20,21,23]
# for i in my_lst:
#     if i%2==0:
#         my_lst.remove(i)       # generally not referred this method for modifying original list
# print(my_lst)

#3. by using lambda function
# my_lst = [22,21,55,63,25,85,66,35,41,21,21,23]
#
# odd = list(filter(lambda x:x%2!=0,my_lst))
# print(odd)

#4. by using list comprehension
# my_lst = [22,21,55,63,25,85,66,35,41,21,21,23]
# lst = [i for i in my_lst if i%2!=0]
# print(lst)

"""
create a list, take a number from user and remove number from
list which is completly divisible by user input.
"""
# my_lst = [10,15,20,25,30,35,50]
# new_lst = []
#
# print(my_lst)
# num = int(input('enter a number:- '))
#
# for i in my_lst:
#     if i%num!=0:
#         new_lst.append(i)
# print(new_lst)

"""
make a list atleast 10 numbers,make two empty list odd and even and put
all the odd numbers in odd list and even numbers in even list.
"""
# lst = [12,15,20,23,21,25,56,20,78,95]
# even_lst = []
# odd_lst = []
#
# for i in lst:
#     if i%2==0:
#         even_lst.append(i)
#     else:
#         odd_lst.append(i)
# print(f'even list {even_lst}')
# print(f'odd list {odd_lst}')

"""
Membership operator in python.

ask number from user and print yes if number exists in list else print no
"""
# lst = [15,54,66,52,23,21,22,55]
#
# num = int(input('enter a number:- '))
# if num in lst:
#     print('yes')
# else:
#     print('no')
















