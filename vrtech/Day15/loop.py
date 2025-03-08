config_lines = ["# This is a comment", "Server=192.168.1.1", "# Another comment", "Port=8080 "]

for value in config_lines:
    if value.startswith('#'):
        continue
    print(value)
