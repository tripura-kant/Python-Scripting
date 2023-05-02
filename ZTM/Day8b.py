class User():
    def sign_in(self):
        print('logged in')


class wizard(User):
    pass


class Archer(User):
    pass


wizard1 = wizard()
print(wizard1.sign_in())
