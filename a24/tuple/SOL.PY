class Solution:
    # @param A : integer
    # @return a double
    def solve(self, A):
        value_pi = 3.146
        result = value_pi * A ** 2
        rounded_result = round(result, 2)  # Round result to 2 decimal places
        return rounded_result


# Create an instance of the Solution class
sol = Solution()

# Call the solve method with input parameter 8
output = sol.solve(8)

# Print the result
print(output)
