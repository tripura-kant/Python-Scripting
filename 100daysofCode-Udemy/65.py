'''
Write a program to find the factors of a given number and check whether the factor is even or odd

'''


def factor_and_even_odd_check(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
            if i % 2 == 0:
                print(f"{i} is even")
            else:
                print(f"{i} is odd")


# taking input from user

num = int(input("Enter a number "))
print(f"The factors of {num} are : ")
factor_and_even_odd_check(num)
