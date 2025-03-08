def print_anti_diagonal(mat, N):
    row = 0
    col = N - 1
    while row < N:
        print(mat[row][col])
        row += 1
        col -= 1
    print()


N = 4
mat = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [1, 2, 3, 4],
       [5, 6, 7, 8]]
print(print_anti_diagonal(mat, N))
