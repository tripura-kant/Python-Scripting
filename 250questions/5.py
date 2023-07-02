# This is file 5.py
#
# def AppendtoList(s):
#   l = [1, 4, 9, 10, 23]
#   l.append(s)
#   return l
#
#
# print(AppendtoList(90))

# l1 = [1, 2, 5, 20]
# print(l1)
#
# l1 = l1 + [90]
# print(l1)

# def getAverage(s):
#   avg = sum(s) / len(s)
#   return avg
#
#
# s = [1, 4, 9, 10, 23]
# print(getAverage(s))

def removeList():
  l1 = [1, 4, 9, 10, 23]
  l2 = [4, 9]
  l1.remove(l2[0])
  l1.remove(l2[1])
  return l1


l1 = removeList()
print(l1)
