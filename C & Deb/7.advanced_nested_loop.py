"""
print following pattern:-
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
"""
# num = 1
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(num,end=' ')
#         num = num+1
#     print()

"""
print following pattern:-
        * 
      * * 
    * * * 
  * * * * 
* * * * * 
"""

# for i in range(1,6):
#     for j in range(i,5):
#         print(' ',end=' ')
#
#     for k in range(1,i+1):
#         print('*',end=' ')
#     print()

"""
print following pattern:-
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 

"""

# for i in range(1,6):
#     for j in range(i,5):
#         print(' ',end=' ')
#
#     for k in range((i*2)-1):
#         print('*',end=' ')
#     print()

"""
print following pattern:-
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 
  * * * * * * * 
    * * * * * 
      * * * 
        * 

"""

for i in range(1,6):
    for j in range(i,5):
        print(' ',end=' ')

    for k in range((i*2)-1):
        print('*',end=' ')
    print()

for i in range(4,0,-1):
    for j in range(5,i,-1):
        print(' ',end=' ')

    for k in range((i*2)-1):
        print('*',end=' ')
    print()
