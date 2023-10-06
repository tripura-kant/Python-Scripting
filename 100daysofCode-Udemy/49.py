decorated_func = new_decorator(func_needs_decorator)


@new_decorator
def func_needs_decorator():
    print('I want to be decorated')


print(func_needs_decorator())
