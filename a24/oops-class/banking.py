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
    def __init__(self, acc_no, name, account_type, balance, branch):
        self.acc_no = acc_no
        self.name = name
        self.account_type = account_type
        self.balance = balance
        self.branch = branch
    