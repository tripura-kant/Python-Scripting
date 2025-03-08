import os

path = "//Python-Scripting/vrtech/Day15/"
files = os.listdir(path)

for index, filename in enumerate(files, start=1):
    full_path = os.path.join(path, filename)  # Ensure full path
    if os.path.isfile(full_path):  # Check if it's a file (not a directory)
        print(index, filename, os.path.getsize(full_path))
