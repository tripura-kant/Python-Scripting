class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):
        start_value = 'B'
        end_value = 'C'

        # Find the indices of the start and end values
        start_index = array.index(start_value)
        end_index = array.index(end_value)

        # Extract the subarray from start_value to end_value (inclusive of start_index and exclusive of end_index + 1)
        subarray = array[start_index:end_index + 1]

        # Print the subarray
        print(subarray)


A = [4, 3, 2, 6]
B = 1
C = 3
