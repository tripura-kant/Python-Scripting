def add_matrices(A, B):
    # Get the number of rows and columns
    rows = len(A)
    cols = len(A[0])

    # Initialize the result matrix with zeros
    result = [[0] * cols for _ in range(rows)]

    # Perform element-wise addition
    for i in range(rows):
        for j in range(cols):
            result[i][j] = A[i][j] + B[i][j]

    return result


# Test with Example Input 1
A1 = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]

B1 = [[9, 8, 7],
      [6, 5, 4],
      [3, 2, 1]]

print("Output 1:")
print(add_matrices(A1, B1))

# Test with Example Input 2
A2 = [[1, 2, 3],
      [4, 1, 2],
      [7, 8, 9]]

B2 = [[9, 9, 7],
      [1, 2, 4],
      [4, 6, 3]]

print("Output 2:")
print(add_matrices(A2, B2))
