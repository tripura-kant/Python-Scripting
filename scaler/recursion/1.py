# Find the sum of n natural number using recursion
def sum(n):
    if n == 0:
        return 0
    return sum(n - 1) + n


n = 5

print(sum(n))


class Solution:
    # @param A: integer
    # @return an integer
    def solve(self, A):
        # Base case: factorial of 0 or 1 is 1
        if A == 0 or A == 1:
            return 1
        # Recursive case: A * factorial of (A - 1)
        return A * self.solve(A - 1)
