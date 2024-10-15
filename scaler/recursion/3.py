# Find the index of B from A . All Indices Of Array
# A = [1, 2, 3, 4, 5]
# B = 1
def all_indices(A, B):
    def help(A, B, idx, count):
        if idx == len(A):
            return [0] * count

        if A[idx] == B:
            count += 1

        ans = help(A, B, idx + 1, count)

        if A[idx] == B:
            ans[count - 1] = idx

        return ans

    return help(A, B, 0, 0)


A = [1, 2, 3, 4, 5, 1]
B = 1

print(all_indices(A, B))
