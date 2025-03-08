import os

path = "//Python-Scripting/vrtech/day8"
files = os.listdir(path)

# Define column widths
col1, col2, col3, col4 = 6, 30, 10, 15

# Print header with alignment
print("SL.no".ljust(col1) + "File Name".center(col2) + "Length".rjust(col3) + "Size (bytes)".rjust(col4))
print("=" * (col1 + col2 + col3 + col4))

cnt = 1
for file in files:
    if file.endswith(".py"):
        file_size = os.path.getsize(os.path.join(path, file))
        print(
            str(cnt).ljust(col1) +
            file.center(col2) +
            str(len(file)).rjust(col3) +
            str(file_size).rjust(col4)
        )
        cnt += 1
