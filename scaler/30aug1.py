class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)

        if n == 0:
            return 0

        # Step 1: Find min and max values
        min_val = min(A)
        max_val = max(A)

        # Initialize the smallest length as a large number
        smallest_length = float('inf')

        # Step 2: Brute-force search
        for start in range(n):
            for end in range(start, n):
                subarray = A[start:end + 1]
                if min_val in subarray and max_val in subarray:
                    smallest_length = min(smallest_length, end - start + 1)

        return smallest_length
