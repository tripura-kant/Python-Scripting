for i in range(1, 251):
    file_name = f"{i}.py"
    with open(file_name, "w") as file:
        file.write("# This is file " + file_name)
