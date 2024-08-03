from typing import Dict, List

details = {
    "Anirudh": [56, 78, 65],
    "Sanjay": [58, 78, 56, 12, 33, 56, 78],
    "Muskan": [87, 78, 65, 45],
    "Nihar": [32, 78, 32, 98, 33],
    "Akshay": [56, 40],
}

# Q1 Print all the marks of each student in a readable format.

# for key, value in details.items():
#     print(f" {key}: {', '.join(str(m) for m in value)}")

# . Print the student name and their corresponding highest marks.
# Anirudh: 78
# Sanjay: 78
# Muskan: 87
# Nihar: 98
# Akshay: 56

# high = 0
# for key, value in details.items():
#     for marks in value:
#         if marks > high:
#             high = marks
#     print(f"{key}: {high}")

# #Q3. Find and print the student(s) with the highest individual score. If
# multiple students have the same highest score, print all their names.
# The highest mark is 98, scored by Nihar.

high = 0
for key, value in details.items():
    for marks in value:
        if marks > high:
            high = max(max(marks) for marks in details.values())
            print(f"{key}: {high}")
