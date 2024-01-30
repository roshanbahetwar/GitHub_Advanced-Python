from random import randint

class Bank:
    print("******* Welcome To SBI Bank *******".center(50))
    def __init__(self):
        self.account = randint(1000000,9999999)
        self.full_name = input("Enter Full Name: ")
        self.phone_number = int(input("Enter Phone Number: "))
        self.balance = 0

    def show_balance(self):
        print(f"Current Balance: {self.balance} Rs")

    def show_details(self):
        print(f"Acoount Number: {self.account}")
        print(f"Account Holder Name: {self.full_name}")
        print(f"Phone Number: {self.phone_number}")
        print(f"Current Balance: Rs {self.balance}")
        print("*"*25)

    def deposit(self):
        amount = int(input("Enter Amount to be deposit: "))
        self.balance = self.balance+amount

    def withdraw(self):
        amount = int(input("Enter Amount to be withdraw: "))
        if amount>self.balance:
            print("Insufficient Balance In Your Account")
        else:
            self.balance -= amount
            print(f"Rs {amount} Withdrawl Succefully Done")
        print(f"Available Balance is: Rs {self.balance}")

banks = []
while True:
    print("Select Menu")
    print("1.Create Account")
    print("2.Deposit Amount")
    print("3.Withdraw Amount")
    print("4.Show Account Details")
    print("5.Exit\n")

    choice = int(input("Enter Choice: "))
    if choice==1:
        x = Bank()
        banks.append(x)
        print("Account Create SuccessFully Done....\n")
    elif choice==2:
        if len(banks)==0:
            print("No Account Created Yet...\n")
        else:
            account_number = int(input("Enter Account Number: "))
            for acc in banks:
                if acc.account == account_number:
                    acc.deposit()
                    print("Amount Deposited successfully Done...")
                    break
    elif choice==3:
        if len(banks)==0:
            print("No Account Created Yet...\n")
        else:
            account_number = int(input("Enter Account Number: "))
            for acc in banks:
                if acc.account==account_number:
                    acc.withdraw()
                    break
    elif choice==4:
        if len(banks)==0:
            print("No Account Created Yet...\n")
        else:
            for acc in banks:
                acc.show_details()
    elif choice==5:
        break
    else:
        print("Invalid Option")