# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#     print(fruit)


# Input a Python list of student heights
# student_heights = input("enter student").split()
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# # 🚨 Don't change the code above 👆

# Write your code below this row 👇
# total_heights = 0
#
# for height in student_heights:
#     total_heights += height
#
# no_st = len(student_heights)
#
# avg_heights = int(total_heights / no_st)
#
# print(f"total height = {total_heights}")
# print(f"number of students = {no_st}")
# print(f"average height = {avg_heights}")

# for loop to find highest score
#
#     # # Input a list of student scores
# student_scores = input("Enter scores    ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
#
# # Write your code below this row 👇
# print(student_scores)
#
# heighest_score = 0
#
# for score in student_scores:
#     if score > heighest_score:
#         heighest_score = score
#
# print(f"The highest score in the class is: {heighest_score}")

# Range

# for number in range(1, 10):
#     print(number)

# total = 0
#
# for number in range(1, 6):
#     total += number
# print(total)

#write a program that calculates the sum of all the even numbers from 1 to X

# target = int(input("enter no  ")) # Enter a number between 0 and 1000
# # 🚨 Do not change the code above ☝️
#
# # Write your code here 👇
#
# sum = 0
# for number in range (0, target+1, 2):
#   sum += number
#
# print(sum)


 #FizzBuzz game.

for num in range(1, 101):
  if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
  elif num % 3 == 0:
    print("Fizz")
  elif num % 5 == 0:
    print("Buzz")
  else:
    print(num)