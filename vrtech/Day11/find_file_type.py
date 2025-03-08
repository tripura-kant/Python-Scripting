fileTypesDict = {
    'py': "Input File Is Python",
    'txt': "Input File Is Text",
    'sh': "nput File Is Shell Script"
}

fileName = input("Enter your filename : ")
ext_file = fileName.rsplit('.', 1)[-1]

print(fileTypesDict.get(ext_file, "Your File Type Is Unkown For Me"))
