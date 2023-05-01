class Playercharater:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f'my name is {self.name}')


player1 = Playercharater('andrei', 100)
print(player1.age)

player2 = Playercharater('monu', 70)
print(player2.name)
player2.speak()

print((1, 2, 3, 1, 2, 3, 1).count(2))
