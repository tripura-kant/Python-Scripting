def position_choice():
    choice = 'wrong'

    while choice not in ['0', '1', '2']:
        choice = input("Pick a position (0,1,2): ")

        if choice not in ['0', '1', '2']:
            print("Sorry invalid choice ")

    return int(choice)


position_choice()
