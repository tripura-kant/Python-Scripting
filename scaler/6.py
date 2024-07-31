def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    num = int(input("enter num "))
    reverse_num = 0
    while num > 0:
        last_digit = num % 10
        reverse_num = (reverse_num * 10) / last_digit
        num = num % 10
        print(reverse_num)
        print(num)
        break


if __name__ == '__main__':
    main()
