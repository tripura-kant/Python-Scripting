for i in range(1, 101):
    file_name = f"{i}.py"
    with open(file_name, "w") as file:
        file.write(f"print('Welcome {file_name}')")
