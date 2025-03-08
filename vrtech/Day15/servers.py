import sys

serverListFile = "/Users/tripurakant/Documents/code/My git/Python-Scripting/vrtech/Day15/server_list.txt"

try:
    with open(serverListFile) as file:
        my_servers = [line.strip() for line in file]

except FileNotFoundError:
    print(f'file is not existing: {serverListFile}')
    sys.exit(1)

print(my_servers)
