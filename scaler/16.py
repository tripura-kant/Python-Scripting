s = "hello"

dic = {}
for ch in s:
    dic[ch] = dic.get(ch, 0) + 1
print(dic)
