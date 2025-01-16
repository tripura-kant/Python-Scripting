# [10, 5]


def rangeSum(A, B):
    def prefix_sum(A):
        n = len(A)
        prefix = [0] * n
        prefix[0] = A[0]

        # calculate prefix sum for the rest of the array
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + A[i]

        return prefix

    prefix = prefix_sum(A)

    result = []

    for query in B:
        l, r = query

        if l == 0:
            result.append(prefix[r])
        else:
            result.append(prefix[r] - prefix[l - 1])
    return result


A = [1, 2, 3, 4, 5]
B = [[0, 3], [1, 2]]
result = rangeSum(A, B)
print(result)
