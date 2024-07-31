def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    T = int(input("enter num "))
    for i in range(1, T + 1):
        n = int(input("enter num "))
        result2 = str(n)[::-1]
        result = int(result2)

        print(result)


if __name__ == '__main__':
    main()
