lst = []
N = int(input("enter"))

for i in range(0, N - 1):
    ele = int(input("enter list"))
    lst.append(ele)
X = int(input("enter"))
Y = int(input("enter"))

lst.insert(X - 1, Y)
print(lst)
