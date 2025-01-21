def count_ag(s):
    result = 0
    n = len(s)
    for i in range(n):
        if s[i] == 'a':
            for j in range(i+1, n):
                if s[j] == 'g':
                    result += 1

    print(result)



s = ['a', 'd', 'g', 'a', 'g', 'a', 'g', 'f', 'g']
count_ag(s)