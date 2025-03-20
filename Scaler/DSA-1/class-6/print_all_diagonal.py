# Print all diagonal from r to l

def print_all_diagonals(mat, N, M):
    for col in range(M):
        start = 0
        end = col
        while start < N and end >= 0:
            print(mat[start][end], end=" ")
            start += 1
            end -= 1
        print()


def main():
    mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    N = 3
    M = 4
    print_all_diagonals(mat, N, M)


if __name__ == "__main__":
    main()
