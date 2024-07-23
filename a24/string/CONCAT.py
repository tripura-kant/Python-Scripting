def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    n = int(input("enter no of time "))
    # print(n)
    result1 = []
    for i in range(n):
        A = input("enter A  ")
        B = input("enter b  ")
        result = A + B
        result1.append(result)
    # print(result1)

    for res in result1:
        print(res)


if __name__ == '__main__':
    main()
