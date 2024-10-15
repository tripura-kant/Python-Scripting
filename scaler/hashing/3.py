A = [2, 3, 4, 54, 5, 6, 1, 2, 1, 2]
q = [2, 3, 10]  # Example list of queries


def find_frequency(A, queries):
    hm = {}

    # Count the frequency of each element in A
    for num in A:
        if num in hm:
            hm[num] += 1
        else:
            hm[num] = 1

    # Check the frequency for each query
    for query in queries:
        if query in hm:
            print(hm[query])  # Print the frequency of the query
        else:
            print(0)  # If query is not in A, print 0


find_frequency(A, q)
