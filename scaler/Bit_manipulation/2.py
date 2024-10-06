# UNSET
class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        num = 1 << B
        if A & num > 0:
            A -= num
        return A
