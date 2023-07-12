# This is file 36.py

# classes

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is %s!" % self.name)


a = Person("Peter", 20)  # instantiation
b = Person("Anna", 19)  # instantiation

a.greet()  # call a's greet method
b.greet()  # call b's greet method

print(a.name)
print(a.age)  # We can also access the attributes of an object

print(b.name)
print(b.age)
