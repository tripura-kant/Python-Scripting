# OOP

class PlayerCharacter:
    def __int__(self, name):
        self.name = name

    def shout(self):
        print(f'my name is {self.name}')


player1 = PlayerCharacter('Cindy', 44)
player2 = PlayerCharacter('tom', 21)
player2.attack = 50

print(player1.shout)

print(player2.name)
