def solve(A, B, C):
    n = len(A)
    s = 0
    e = n - B  # Calculate the maximum index where a subarray of size B can start

    # Loop over all possible subarray starting points
    for i in range(s, e + 1):
        current_sum = 0
        for j in range(i, i + B):
            current_sum += A[j]

        # If a subarray sum equals C, print 1 and exit the function
        if current_sum == C:
            print(1)
            return  # Exit the function immediately once we find a match

    # If no subarray sum equals C, print 0
    print(0)


# Test case
A = [4, 3, 2, 6, 1]
B = 3
C = 11
solve(A, B, C)
