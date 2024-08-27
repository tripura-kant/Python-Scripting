class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return : list of integers
    def solve(self, A, B):
        N = len(A)
        k = B % N  # Effective number of rotations

        if k == 0:
            return A  # No need to rotate

        # Create a new array for the result
        result = [0] * N

        # Populate the new array with rotated values
        for i in range(N):
            new_position = (i + k) % N
            result[new_position] = A[i]

        return result


# Example usage
A = [7, 4, 2, 10, 5]
B = 10
res = Solution()
rotated_array = res.solve(A, B)
print(rotated_array)  # Expected output: [7, 4, 2, 10, 5]
