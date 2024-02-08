'''
Write a program that will find all the numbers between 1000 and 3000 (both excluded)
such that each digit of a number is an odd number.
Print the number of such elements
'''

count = 0

for num in range(1001, 3000):
    num_str = str(num)

    all_odd = True

    for digit in num_str:
        if int(digit) % 2 == 0:
            all_odd = False
            break
    if all_odd:
        print(num)
        count += 1

print("Total count :", count)
