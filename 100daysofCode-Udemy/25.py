# Milestone Project Tic toc toe


def display(row1, row2, row3):
    print(row1)
    print(row2)
    print(row3)


row1 = ['', '', '']
row2 = ['', '', '']
row3 = ['', '', '']

row2[0] = 'X'
display(row1, row2, row3)


def user_choice():
    choice = input("Enter a number (0-10): ")
    return int(choice)


user_choice()
