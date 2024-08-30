class Solution:
    # @param A : list of integers
    # @param B : 2D list of integers
    # @return a list of integers
    def solve(self, A, B):
        n = len(A)
        m = len(B)

        # Step 1: Compute prefix sums
        prefix_sum = [0] * n
        prefix_sum[0] = A[0]

        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + A[i]

        # Step 2: Process queries
        results = []
        for L, R in B:
            if L == 0:
                results.append(prefix_sum[R])
            else:
                results.append(prefix_sum[R] - prefix_sum[L - 1])

        return results


# Example usage
solution = Solution()
A1 = [1, 2, 3, 4, 5]
B1 = [[0, 3], [1, 2]]
print(solution.solve(A1, B1))  # Output: [10, 5]

A2 = [2, 2, 2]
B2 = [[0, 0], [1, 2]]
print(solution.solve(A2, B2))  # Output: [2, 6]
