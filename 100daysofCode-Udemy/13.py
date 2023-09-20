def myfunc(input_string):
    result = ""
    for i, letter in enumerate(input_string):
        if i % 2 == 0:
            result += letter.lower()
        else:
            result +=letter.upper()
    return result
input_string = "ASsaSasaSASDDASD"
print(myfunc(input_string))