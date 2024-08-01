class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

    def is_square(self):
        if (self.length == self.breadth):
            return True
        return False


r1 = Rectangle(5, 10)
print(r1.area())
print(r1.perimeter())
print(r1.is_square())
