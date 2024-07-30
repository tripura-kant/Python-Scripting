my_dict = {
    "Anirudh": {
        "age": 56,
        "marks": [3, 40, 56]
    },
    "Muskan": {
        "age": 16,
        "marks": [13, 40, 56]
    },
}
# for name, info in my_dict.items():
#     # print(info["age"])
#     print(f'{name} has scored {sum(info["marks"])}')

'''
Anirudh has 56 marks
Muskan has 100 marks
'''

for name, info in my_dict.items():
    total = 0
    for mark in info["marks"]:
        total = total + mark
    print(f'{name} has scored {total} marks')
