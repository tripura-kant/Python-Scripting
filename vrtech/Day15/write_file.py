file = 'demo.txt'

# with open(file, 'w') as file:
#     file.write("This is first line\n")


my_list_lines = ['frist', 'second', 'third']
# mylistlines=[]
# for eachvalue in my_list_lines:
#     mylistlines.append(eachvalue+'\n')

with open(file, 'w') as file:
    # file.write("This is first line\n")
    for eachline in my_list_lines:
        file.write(eachline + "\n")
