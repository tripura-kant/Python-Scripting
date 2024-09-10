class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):
        # Get the number of rows and columns of the input matrix
        m = len(A)
        n = len(A[0])

        # Create the transposed matrix with dimensions n x m
        transposed = [[0] * m for _ in range(n)]

        # Fill the transposed matrix
        for i in range(m):
            for j in range(n):
                transposed[j][i] = A[i][j]

        return transposed
