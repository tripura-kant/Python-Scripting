# def main():
#     # YOUR CODE GOES HERE
#     # Please take input and print output to standard input/output (stdin/stdout)
#     # E.g. 'input()/raw_input()' for input & 'print' for output
#     T = int(input("ENTER T "))
#     for i in range(1, T + 1):
#         A = int(input("ENTER N1"))
#         B = int(input("ENTER N2"))
#         x = min(A, B)
#         for i in range(x, 0, -1):
#             if (A % i == 0 and B % i == 0):
#                 print(i)
#                 break
#
#
# if __name__ == '__main__':
#     main()
# def main():
#     # YOUR CODE GOES HERE
#     # Please take input and print output to standard input/output (stdin/stdout)
#     # E.g. 'input()/raw_input()' for input & 'print' for output
#     T = int(input("ENTER T "))
#     for i in range(1, T + 1):
#         A = int(input("ENTER N1"))
#         B = int(input("ENTER N2"))
#         x = max(A, B)
#         while True:
#             if (x % A == 0 and x % B == 0):
#                 print(x)
#                 break
#             x += 1
#
#
# if __name__ == '__main__':
#     main()

def main():
    T = int(input())
    for _ in range(T):
        A = int(input())
        B = int(input())
        x = max(A, B)
        while True:
            if x % A == 0 and x % B == 0:
                print(x)
                break
            x += 1


if __name__ == "__main__":
    main()
