def sumofevenindex(arr, queries, n):
    PSe = [0] * n
    PSe[0] = arr[0]

    # create psum array for even indexed elements
    for i in range(1, n):
        if i % 2 == 0:
            PSe[i] = PSe[i - 1] + arr[i]
        else:
            PSe[i] = PSe[i - 1]

    # Process the query
    for query in queries:
        l = query[0]
        r = query[1]

        if l == 0:
            print(PSe[r])
        else:
            print(PSe[r] - PSe[l - 1])


# example
arr = [1, 2, 3, 4, 5, 6]
queries = [[0, 2], [1, 4]]
n = len(arr)

sumofevenindex(arr, queries, n)
