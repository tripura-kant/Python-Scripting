def unique_count(tup):
    lst = []
    for v in tup:
        # We got v first time
        if v not in lst:
            lst.append(v)
            print(v, ':', tup.count(v))


tup = (100, -10, -10, "ONE", [22], [22], "ONE")
unique_count(tup)
