# Inheritance

class Animal():
    def __init__(self):
        print('hiiiiii')

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")

myanimal = Animal()

print(myanimal.eat())
print(myanimal)
print(myanimal.who_am_i())
