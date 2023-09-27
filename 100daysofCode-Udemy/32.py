class Dog():
    species = 'mammal'

    def __init__(self, bread, name):
        self.bread = bread
        self.name = name

    def bark(self):
        print("whooo!")


my_dog = Dog(bread='lal', name='tomy')
print(my_dog.name)
print((my_dog.bread))
print(my_dog.bark())
