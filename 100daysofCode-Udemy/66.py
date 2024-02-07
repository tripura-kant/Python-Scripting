'''
2.Write a code that accepts a sequence of words as input and prints the words in a
 sequence after sorting them alphabetically.Hint: 
Use split() to split the string into a list and then apply sort()
'''


def sort_alphabet(string):
    string1 = string.split()
    print(string1)
    x = sorted(string1)
    print(x)
    print("Words sorted alphabetically:")
    print(' '.join(x))


string = input("Enter words ")
sort_alphabet(string)
