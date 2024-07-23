# def main():
#     # YOUR CODE GOES HERE
#     # Please take input and print output to standard input/output (stdin/stdout)
#     # E.g. 'input()/raw_input()' for input & 'print' for output
#     num1 = int(input("enter"))
#     result = num1 * 2
#     result1 = print(result)
#     return result1
#
#
# if __name__ == '__main__':
#     main()


# Write a program to input an integer T and then each of T lines will have 2 strings (A and B).
#
# You have to concatenate two strings and print T lines each containing concatenated string.
#

def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    n = int(input("enter no of line "))
    for i in range(n):
        a, b = input("string").split()
        concaternation = a + b
        result = print(concaternation)
    return result


if __name__ == '__main__':
    main()

# input1=int(input())

# input1 = int(input())
# input2 = int(input())
# input3 = int(input())
