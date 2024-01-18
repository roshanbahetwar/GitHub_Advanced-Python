# class 51 and 52
"""
write a programme to reverse a word
"""
# my_string = 'python is good'
#
# words = my_string.split()
# words = words[::-1]
# result = ' '.join(words)
# print(result)

"""
write a programme to each first letter should be capital.
"""
# my_string = "python is GOOD"
# words = my_string.split()
# result = ' '.join(str(i).capitalize() for i in words)
# print(result)
"""
write a programme output should be, nohtyp si DOOG.
"""
# my_string = "python is GOOD"
# words = my_string.split()
# result = ' '.join(str(i)[::-1] for i in words)
# print(result)

"""
write a programme, input :- "helloWorldHowAreYou", and
output should in,  hello_world_how_are_you.
"""
# my_string = "helloWorldHowAreYou"
# result = ''
# #1.
# for i in my_string:
#     if i.isupper():
#         result = result+'_'+ i.lower()
#     else:
#         result = result+i
# print(result)
#
# #2.
# words = ''.join("_"+i.lower() if i.isupper() else i for i in my_string)
# print(words)

