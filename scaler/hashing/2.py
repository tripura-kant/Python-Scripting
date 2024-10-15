# # Hash set
# my_set = set()
#
# my_set.add(5)
# my_set.add(649)
#
# print(my_set)
#
# # search
#
# if 649 in my_set:
#     print("24 is present")


# mymap = {}
# mymap[1] = 4
# if 1 in mymap:
#     print("Yes")
# if 2 not in mymap:
#     print("YESS!")

mymap = {}
mymap[1] = 4
mymap[3] = 5

for key in mymap:
    print(key, end=', ')
    print(mymap[key])
