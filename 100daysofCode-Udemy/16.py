# Write a function that capitalizes the first and fourth letter of a name

def old_macdonald(name):
    first_letter = name[0]
    in_between = name[1:3]
    fourth_letter = name[3]
    rest = name[4:]

    return first_letter.upper() + in_between + fourth_letter.upper() + rest

print(old_macdonald('macdonald'))

