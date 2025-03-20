class calculator(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def addition(self, x, y):
        return x + y

    def substraction(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y


x = 20
y = 23
mycalculator = calculator(x, y)
print(mycalculator.addition(x, y))
print(mycalculator.multiply(x, y))
