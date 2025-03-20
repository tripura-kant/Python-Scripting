def process_matrix(A):
    n = len(A)
    m = len(A[0])
    print(n)
    print(m)


def main():
    A = [[1, 2, 3, 4], [5, 6, 7, 0], [9, 2, 0, 4]]
    result = process_matrix(A)

    # for row in result:
    #     print(row)


if __name__ == "__main__":
    main()
