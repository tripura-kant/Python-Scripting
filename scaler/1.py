def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    a = int(input("enter "))
    b = int(input("enter "))
    c = int(input("enter "))

    if a + b > c and a + c > b and b + c > a:
        print(1)
    else:
        print(0)


if __name__ == '__main__':
    main()
