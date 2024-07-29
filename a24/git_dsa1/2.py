# # n = 100
# # i = 1
# # while i * i <= n:
# #     print(i * i)
# #     i += 1
#
# for i in range(-6, -10, -1):
#     print(i, end=" ")

def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    n = 5
    i = 1
    sum = 0
    while i <= n:
        sum = sum + i
      i += 1

    print(sum)


if __name__ == '__main__':
    main()
