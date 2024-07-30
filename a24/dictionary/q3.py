"""
Anirudh has scored 180 marks
"""
details = {
    "anirudh": [23, 40, 99],
    "rahul": [70, 89, 100]
}

# sum = 1
# result = []
# for key, value in details.items():
#     result = details[key]
#     print(result)
#     for i in result:
#         sum = sum + i
#         i += 1
#
# print(sum)

for name, marks in details.items():
    # print(f"{name} has scored {sum(marks)}")
    total = 0
    for marks in marks:
        total = total + marks

    print(f"{name} has scored {total}")
    print(total)
