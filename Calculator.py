# Store calculator

sum = 0
while True:
    userInput = input('Enter the item Price or press q to quite :- ')

    if userInput != 'q':
        sum = sum + int(userInput)
    else:
        print('Thanks for shopping...\nYour Total Bill is:- ',sum)
        break