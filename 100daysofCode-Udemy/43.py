## Error and handling homework solution lecture

def ask():
    # Waiting for correct response
    waiting = True
    while waiting:
        try:
            n = int(input('Enter a number '))
        except:
            print('Please try again')
            continue
        else:
            waiting = False

    print('Your number square is: ')
    print(n ** 2)


ask()
