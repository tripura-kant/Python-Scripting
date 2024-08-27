class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        res = 0
        for i in range(n):
            if B == A[i]:
                res += 1
        return res


A = [1, 2, 2]
B = 2
n = len(A)
result = Solution()
print(result.solve(A, B))
