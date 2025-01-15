class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B, ):
        count = 0
        n = len(A)
        for i in A:
            if B == i:
                count += 1

        return count
