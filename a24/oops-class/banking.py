"""
Menu
1) Add a account
    acc_no = int
    name = str
    account_type str (saving/current)
    balance
    branch

2) Display all account
3) Exit
"""


class Banking:
    def __init__(self, acc_no, name, account_type, branch):
        self.acc_no = acc_no
        self.name = name
        self.account_type = account_type
        self.balance = 0
        self.branch = branch

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Updated balace is {self.balance}")

    def display(self):
        print(f"acc_no = {self.acc_no}")
        print(f"Name = {self.name}")
        print(f"account_type = {self.account_type}")
        print(f"balance = {self.balance}")
        print(f"branch = {self.branch}\n\n")


bank_details = []
while True:
    print("1) Add a account")
    print("2) Display all account")
    print("3) Exit")
    print("4) Get balance")
    print("5) Deposit")

    choice = int(input("Enter your choice = "))
    if choice == 1:
        acc_no = int(input("Enter acc_no = "))
        name = input("Enter name = ")
        account_type = input("Enter account_type = ")
        branch = input("Enter branch = ")

        x = Banking(acc_no, name, account_type, branch)
        bank_details.append(x)

    elif choice == 2:
        if len(bank_details) == 0:
            print("No account found")
        else:
            for acc in bank_details:
                acc.display()

    elif choice == 4:
        acc_no = int(input("ENter acc no"))
        for acc in bank_details:
            if acc.acc_no == acc_no:
                print(f"Your balace is {acc.get_balance()}")

    elif choice == 5:
        acc_no = int(input("ENter acc no"))
        amount = int(input("Enter deposit amount"))
        for acc in bank_details:
            if acc.acc_no == acc_no:
                acc.deposit(amount)
                print(f"Your balace is {acc.get_balance()}")

    elif choice == 3:
        print("Exiting bank application    ")
        break
    else:
        print("Invalid Choice")
