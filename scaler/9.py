def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    n = 4
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            if j < i:
                print(j, end=" ")
            else:
                print(j, end="")  # No space after the last number

        print()


if __name__ == '__main__':
    main()
