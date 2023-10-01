class cyclinder:

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return self.height * 3.14 * (self.radius) ** 2

    def surface_area(self):
        top = 3.14 * (self.radius ** 2)

        return (2 * top) + (2 * 3.14 * self.radius * self.height)


mycyclinder = cyclinder(2, 3)

print(mycyclinder.volume())
