print('Welcome 73.py')

motorcycles = []

flag = 'C'

while flag == 'c' or flag == 'C':
    name = input("Enter a motorcycle name :: ")
    motorcycles.append(name)
    flag = input("Enter C: continue, P: printing the list, any other to break: ")
    if flag == 'P' or flag == 'p':
        print("The name of motor cycles are: ", motorcycles)
