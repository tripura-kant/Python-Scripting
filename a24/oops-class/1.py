class Student:
    id = 0
    name = ""
    age = 30
    gender = ""

    def display(self):
        print(self)
        print(f"ID = {self.id}")
        print(f"name = {self.name}")
        print(f"age = {self.age}")


s1 = Student()
s1.name = "Tripura"

s1.display()
