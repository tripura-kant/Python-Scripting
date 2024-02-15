import os

file_path = '/Users/tripurakant/Documents/Imp-folder/py/Python-Scripting/100daysofCode-Udemy/File_new.txt'

try:
    with open(file_path, mode='w') as myfile:
        for i in range(1, 5, 3):
            myfile.write("The file is opened in write mode")

    print("File created successfully at:", file_path)
except Exception as e:
    print("An error occurred:", str(e))
    # Remove the file if an error occurs
    os.remove(file_path)
