def pattern(N):
    for i in range(1, N + 1):
        for j in range(i, N + 1):
            if i == 1 or j == i or j == N:
                print("j", end=" ")
            else:
                print(" ", end=" ")
        print()


# Driver code
if __name__ == "__main__":
    N = 6
    pattern(N)
