# Python Program to count occurrence of characters in string

string1 = "python"

char = "y"
count = 0
for i in range(len(string1)):
    if (string1[i] == char):
        count = count + 1
print(count)
