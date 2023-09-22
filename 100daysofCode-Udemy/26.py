def user_choice():
    choice = 'WRONG'
    while choice.isdigit() == False:
        choice = input("Please enter a num (1-10): ")
        if choice.isdigit() == False:
            print("Sorry not a digit")
        else:
            print('iTS A DIGIT')

    return int(choice)


user_choice()
