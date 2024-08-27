class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):
        i, j = B, C
        while i < j:
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
            i, j = i + 1, j - 1
        return A


A = [1, 2, 3, 4]
B = 2
C = 3
sol = Solution()
print(sol.solve(A, B, C))
