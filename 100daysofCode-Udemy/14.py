def animal_crackers(text):
    wordlist = text.split()
    print(wordlist)

    first_list = wordlist[0]
    second_list = wordlist[1]

    return first_list[0] == second_list[0]


print((animal_crackers('hi, honu')))