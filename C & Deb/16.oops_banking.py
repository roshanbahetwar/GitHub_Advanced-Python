from random import randint

class Bank:
    def __init__(self)->None:
        self.account_number = randint(1000000,9999999)
        self.full_name = input("Enter Full Name: ")
        self.phone_number = int(input("Enter phone number: "))
        self.balance = 0

    def show_balance(self)->None:
        print(f"Current Balance: {self.balance} Rs.")

    def withdraw(self)->None:
        amount = int(input("Enter amount to withdraw: "))
        if amount>self.balance:
            print("Insufficient balance.")
        else:
            self.balance = self.balance-amount

    def deposit(self)->None:
        amount = int(input("Enter amount to be deposit: "))
        self.balance = self.balance+amount

    def account_details(self):
        print("*"*25)
        print("Account Details")
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder Name: {self.full_name}")
        print(f"Phone Number: {self.phone_number}")
        print(f"Balance: {self.balance}")
        print("*" * 25,"\n")

banks = []
while True:
    print("1. Create Account")
    print("2. Show Account Details")
    print("3. Deposit Amount")
    print("4. Exit")
    choice = int(input("Enter Choice: "))

    if choice==1:
        x = Bank()
        banks.append(x)
    elif choice==2:
        if len(banks)==0:
            print("No account created yet.")
        else:
            for account in banks:
                account.account_details()
    elif choice==3:
        if len(banks)==0:
            print("No account has been created yet.")
        else:
            acc_no = int(input("Enter Account Number: "))
            for acc in banks:
                if acc.account_number==acc_no:
                    acc.deposit()
                    break
    elif choice==4:
        break