with open('sample.csv', 'r') as file:
    for eachline in file:
        print(eachline.strip().split(',')[0])
