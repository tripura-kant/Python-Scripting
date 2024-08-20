import math


class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        count = 0
        sqrt_A = int(math.sqrt(A))
        for i in range(1, sqrt_A + 1):
            if A % i == 0:
                if i * i == A:
                    count += 1
                else:
                    count += 2
        return count


A = 637759701
x = Solution()
print(x.solve(A))
