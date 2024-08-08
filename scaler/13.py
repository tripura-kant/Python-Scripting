s = [2, 0, 1]

rev_s = [0] * len(s)
for key, value in enumerate(s):
    rev_s[value] = key

print(rev_s)
