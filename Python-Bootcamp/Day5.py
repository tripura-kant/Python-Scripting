# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#     print(fruit)


# Input a Python list of student heights
student_heights = input("enter student").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
total_heights = 0

for height in student_heights:
    total_heights += height

no_st = len(student_heights)

avg_heights = int(total_heights / no_st)

print(f"total height = {total_heights}")
print(f"number of students = {no_st}")
print(f"average height = {avg_heights}")