'''
x = rectangle (5,8) # (l, b)
ans = x.area()
x.is_square() # boolean
answ=x.perimeter 2 (l+b)



'''


class rectangle:

    def __init__(self):
        self.length = int(input("Enter length "))
        self.breadth = int(input("Enter breadth "))

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

    def is_square(self):
        if (self.length == self.breadth):
            return True


r1 = rectangle()
print(r1.area())
print(r1.perimeter())
print(r1.is_square())
