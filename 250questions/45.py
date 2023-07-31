# This is file 45.py

# class inheritance


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def getsalary(self):
        print(self.salary)


rohan = Employee("Rohan", "23333")

print(rohan.salary)
print(rohan.name)

rohan.getsalary()
