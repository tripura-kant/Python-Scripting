# Python scripting
fo =  open('demo.txt', 'r')
# print(fo.read())
# fo.close()

for each_line in fo.readlines():
    if "error" in each_line:
        print(each_line)
fo.close()    