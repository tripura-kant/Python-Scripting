def shift():
    n = 5  # Read the number of elements
    a = list(map(int, input().split()))  # Read the list of integers

    # Create a new list with the last element at the beginning
    shifted_a = [a[-1]] + a[:-1]

    # Print the elements with proper spacing
    for i in range(n):
        print(shifted_a[i], end=" ")  # Print the current element


# Example usage
if __name__ == "__main__":
    shift()
