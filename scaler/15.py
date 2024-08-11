def main():
    n = int(input())
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    for i in range(n):
        for j in range(n - 1):
            if j == 0 or j == n - i - 1 or i == 0:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


if __name__ == '__main__':
    main()
