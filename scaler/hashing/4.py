A = [10, 3, 5, 6, 9]


def check_freq(A):
    s = set()
    for i in range(len(A)):
        s.add(A[i])

    return len(s)


print(check_freq(A))
