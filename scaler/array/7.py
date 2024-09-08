class Solution:
    # @param A : list of list of integers
    def solve(self, A):
        n = len(A)

        # Step 1: Transpose the matrix
        for i in range(n):
            for j in range(i + 1, n):
                A[i][j], A[j][i] = A[j][i], A[i][j]

        # Step 2: Reverse each row
        for i in range(n):
            A[i].reverse()

        return A


# Example usage:
sol = Solution()
matrix1 = [
    [1, 2],
    [3, 4]
]

matrix2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(sol.solve(matrix1))  # Output: [[3, 1], [4, 2]]
print(sol.solve(matrix2))  # Output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
