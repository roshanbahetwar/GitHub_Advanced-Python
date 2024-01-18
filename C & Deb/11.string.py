# class 49 and 50
"""
ask a string from user, count how many alphabets are there in that strings
"""
#
# my_string = 'abc1254'
#
# count = 0
# for char in my_string:
#     if char.isalpha():
#         count = count + 1
# print(count)

"""
ask a string from user, count the number of uppercase and lowercase
character in that string.
"""
# my_string = "abc1253ABCD"
#
# upper_count = 0
# lower_count = 0
#
# for char in my_string:
#     if char.isupper():
#         upper_count = upper_count+1
#     elif char.islower():
#         lower_count = lower_count+1
#
# print(f'uppercase char:- {upper_count}')
# print(f'lowercase char:- {lower_count}')

"""
count alphabates,digit and space in given string from users
"""
# userInput = input("enter string:- ")
# dig_count = 0
# alp_count = 0
# sp_count = 0
#
# for char in userInput:
#     if char.isdigit():
#         dig_count += 1
#     elif char.isalpha():
#         alp_count += 1
#     elif char.isspace():
#         sp_count += 1
# print(dig_count)
# print(alp_count)
# print(sp_count)

#***join and split***
#
# my_string = "hello this is python world"
#
# words = my_string.split()
# for char in words:
#     print(f'{char}:- {len(char)}')

# my_string = "hello this is python world"
#
# dict = {}
# words = my_string.split()
# for char in words:
#     dict[char] = len(char)
# print(dict)

# my_string = "hello-this-is-python-world"
#
# words = my_string.split('-')
# print(words)

# lst = [15,25,35,'hello','this','world']
# words = ''
# for i in lst:
#     words = words +' '+ str(i)
# print(words)
lst = [15,25,35,'hello','this','world']

words = ' '.join(str(i).title() for i in lst)
print(words)



