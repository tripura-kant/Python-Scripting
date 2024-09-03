def compute_prefix_sum(A):
    n = len(A)

    for i in range(1, n):
        A[i] += A[i - 1]

    return A


A = [1, 2, 3, 4]
print(compute_prefix_sum(A))
