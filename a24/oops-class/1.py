class Student:
    idd = 0
    name = ""
    age = 30
    gender = ""

    def display(self):
        print(self)
        print(f"ID = {self.idd}")
        print(f"name = {self.name}")
        print(f"age = {self.age}")
        print(f"gender = {self.gender}")


s1 = Student()
s2 = Student()
s1.name = "Tripura"
s1.age = 99
s1.gender = "Male"

# s1.display()
s2.display()
