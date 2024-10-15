class Solution:
    def PrintArray(self, A):
        # Helper function to print elements recursively
        def print_helper(index):
            if index == len(A):
                print()  # Print a new empty line at the end
                return

            print(A[index])  # Print the current element
            print_helper(index + 1)  # Recursive call for the next element

        print_helper(0)  # Start printing from index 0


# Example usage
solution = Solution()
A = [1, 2, 3, 4, 5]
solution.PrintArray(A)
