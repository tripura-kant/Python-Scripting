n = int(input("Enter no of subject "))

result = {}
for i in range(n):
    sub = input("enter subject")
    marks = input("Enter marks")
    result[sub] = marks

formatted_result = {f"{key}": f"{value}" for key, value in result.items()}
print(formatted_result)
