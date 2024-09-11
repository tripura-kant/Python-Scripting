from typing import List


def getSecondOrderElements(arr):
    a = arr
    small = float("inf")
    second_small = float("inf")
    large = float("-inf")
    second_large = float("-inf")

    for i in range(0, len(arr)):
        if a[i] < small:
            second_small = small
            small = a[i]
        elif a[i] < second_small and a[i] != small:
            second_small = a[i]
        if a[i] > large:
            second_large = large
            large = a[i]
        elif a[i] > second_large and a[i] != large:
            second_large = a[i]

    return [second_large, second_small]


arr = [1, 2, 3, 4, 5]
print(getSecondOrderElements(arr))
