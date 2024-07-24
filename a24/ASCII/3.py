my_string = "asdadas djkhask 123%%%%@"


# count digit,alphatbet space symbol

def count_char(my_string):
    alphabet = 0
    digit = 0
    space = 0
    symbol = 0

    for ch in my_string:
        ascii_code = ord(ch)
        if 97 <= ascii_code <= 122:
            alphabet += 1
        elif 65 <= ascii_code <= 90:
            alphabet += 1
        elif ascii_code >= 48 and ascii_code <= 57:
            digit += 1
        elif ascii_code == 32:
            space += 1
        else:
            symbol += 1
    print(f"Alphabet = {alphabet}, Digits = {digit}, Space = {space}, Symbol = {symbol}")


count_char(my_string)
