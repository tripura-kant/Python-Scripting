file_obj = open('File2.txt', 'r')
print(file_obj.tell())
file_obj.read()
print(file_obj.tell())
output = file_obj.read()
while True:
    for i in output:
        print(output)
    break
