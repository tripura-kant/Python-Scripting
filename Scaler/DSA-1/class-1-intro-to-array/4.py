# function to reverse the array from start to end
def reverse(arr, start, end):
    left = start
    right = end
    while left < right:
        # swap the elements
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1


# function to rotate the array
def rotate(arr, k):
    N = len(arr)  # size of the array
    k = k % N  # this will handle when value of k>N

    # step 1:reverse the whole array
    reverse(arr, 0, N - 1)

    # step 2: reverse the first k elements
    reverse(arr, 0, k - 1)

    # step 3: reverse the remaining elements
    reverse(arr, k, N - 1)


# Example usage
if __name__ == "__main__":
    arr = [5, -4, 8, 9, 10]
    k = 2  # no of rotations
    print("Original Array:", arr)

    # rotate the array k times
    rotate(arr, k)
    print("Array after k rotations:", arr)
