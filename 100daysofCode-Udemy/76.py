# class

# class fruit:
#     color = "red"
#     stem = "yes"
#
#
# apple = fruit()
# print(apple.stem)


class shark():
    # class level
    animal_type = "fish"
    location = "ocean"

    def setfunc(self, name, age, size):
        # Instance level
        self.name = name
        self.age = age
        self.size = size


print('class example')
print('*' * 20)
sammy = shark()
sammy.setfunc("Sammy", 5, 10.5)

print(sammy.animal_type, sammy.location, sammy.name, sammy.age, sammy.size)
