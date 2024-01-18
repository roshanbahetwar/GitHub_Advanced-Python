# class 29 and 30

"""
print following pattern:-

* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
"""
# for i in range(1,6):
#     for j in range(1,6):
#         print('*',end='')
#     print()

"""
print following pattern:-

1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
"""
# for i in range(1,6):
#     for j in range(1,6):
#         print(j,end=' ')
#     print()

"""
print following pattern:-
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
"""
# for i in range(1,6):
#     for j in range(5,0,-1):
#         print(j,end=' ')
#     print()
"""
print following pattern:-
1 1 1 1 1 
2 2 2 2 2 
3 3 3 3 3 
4 4 4 4 4 
5 5 5 5 5 
"""
# for i in range(1,6):
#     for j in range(1,6):
#         print(i,end=' ')
#     print()

"""
print following pattern:-
5 5 5 5 5 
4 4 4 4 4 
3 3 3 3 3 
2 2 2 2 2 
1 1 1 1 1 
"""

# for i in range(5,0,-1):
#     for j in range(1,6):
#         print(i,end=' ')
#     print()

"""
ask a number from user means no. of lines
and print it,
ex:-
enter a number:- 8
1 1 1 1 1 
2 2 2 2 2 
3 3 3 3 3 
4 4 4 4 4 
5 5 5 5 5 
6 6 6 6 6 
7 7 7 7 7 
8 8 8 8 8 
"""

# n = int(input('enter a number:- '))
#
# for i in range(1,n+1):
#     for j in range(1,6):
#         print(i,end=' ')
#     print()

"""
ask a number from user means no. of lines
and print it,
ex:- 
enter a number:- 8
8 8 8 8 8 
7 7 7 7 7 
6 6 6 6 6 
5 5 5 5 5 
4 4 4 4 4 
3 3 3 3 3 
2 2 2 2 2 
1 1 1 1 1 

"""
#
# n = int(input('enter a number:- '))
#
# for i in range(n,0,-1):
#     for j in range(1,6):
#         print(i,end=' ')
#     print()

"""
print following pattern:-
1
1,2
1,2,3
1,2,3,4
1,2,3,4,5
"""
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=' ')
#     print()

"""
print following pattern:-
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 
"""
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i,end=' ')
#     print()

"""
print following pattern:-
1 
2 1 
3 2 1 
4 3 2 1 
5 4 3 2 1 
"""
# for i in range(1,6):
#     for j in range(i,0,-1):
#         print(j,end=' ')
#     print()

"""
print following pattern:-
5 
5 4 
5 4 3 
5 4 3 2 
5 4 3 2 1 
"""
# for i in range(5,0,-1):
#     for j in range(5,i-1,-1):
#         print(j,end=' ')
#     print()

"""
print following pattern:-
5 
4 4 
3 3 3 
2 2 2 2 
1 1 1 1 1
"""
# for i in range(5,0,-1):
#     for j in range(5,i-1,-1):
#         print(i,end=' ')
#     print()

"""
print following pattern:-
5 4 3 2 1 
5 4 3 2 
5 4 3 
5 4 
5
"""

# for i in range(1,6):
#     for j in range(5,i-1,-1):
#         print(j,end=' ')
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
#     for j in range(1,i+1):
#         print('*',end=' ')
#     print()

"""
print following pattern:-
* * * * * 
* * * * 
* * * 
* * 
* 
"""

# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print('*',end=' ')
#     print()

"""
print following pattern:-
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1 
"""
# for i in range(5,0,-1):
#     for j in range(i,0,-1):
#         print(j,end=' ')
#     print()

"""
print following pattern:-
1 
2 1 
3 2 1 
4 3 2 1 
5 4 3 2 1 
"""

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=' ')
    print()




