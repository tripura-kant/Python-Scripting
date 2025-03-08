# with open('sample.csv', 'r') as file:
#     for eachline in file:
#         print(eachline.strip().split(',')[0])

import csv

with open("sample.csv", "r") as file:
    reader = csv.reader(file, delimiter="|")
    for eachrow in reader:
        print(eachrow)
