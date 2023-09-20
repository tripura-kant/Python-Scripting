#print('Welcome 7.py')

def check_even_list(num_list):
    even_numbers = []
    for number in num_list:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            pass
    return even_numbers
print(check_even_list([20,42,21,97]))