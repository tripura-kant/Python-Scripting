def func():
    return 1


# print(func())


def hello(name='Jose'):
    print('The hello() function has been executed. ')

    def greet():
        return '\t This is the greet() function inside hello!'

    def welcome():
        return '\t This is welcome() function inside hello'

    if name == 'Jose':
        return greet
    else:
        return welcome

    # print(greet())
    # print(welcome())


my_new_func = hello('Jose')
print(my_new_func())
