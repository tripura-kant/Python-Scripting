listOfFiles = ["demo.txt", 'hello.py', "new.bat", 'new.py']

list_of_py_file = []
cnt = 1

for each_value in listOfFiles:
    print(f'{cnt} / {len(listOfFiles)} working on {each_value}')
    if each_value.endswith(".py"):
        print(f'{each_value} is a python file')
        list_of_py_file.append(each_value)
    cnt += 1
print(list_of_py_file)
