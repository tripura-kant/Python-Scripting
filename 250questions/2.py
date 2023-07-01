print("Given a MathOp() function, try the following mathematical calculations and print the output:")
# (3 / 2)
# (3 // 2)
# (3 % 2)
# (3**2)


def MathOp():
    division = 3/2
    modulo = 3//2
    modulus = 3 % 2
    power = 3 ** 2
    return [division,modulo,modulus,power]

[division, modulo, modulus, power]=MathOp()
print(division)




