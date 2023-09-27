class Dog():
    def __init__(self, bread, name, spots):
        self.bread = bread
        self.name = name
        self.spots = spots


my_dog = Dog(bread='lab', name='Sammy', spots=False)

print(my_dog.name)
