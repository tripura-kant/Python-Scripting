# sentence = "The quick brown fox jumped over the lazy dog."
# sentence = sentence.split(" ")
# characters = {}
#
# for character in sentence:
#     characters[character] = characters.get(character, 0) + 1
#
# print(characters)


def list_to_dict(keys, values):
    # write your code here
    dict = {}
    for i in keys:
        for j in values:
            dict[i] = j
            values.remove(j)
            break

    print(dict)


keys = [1, 2, 3]
values = [4, 5, 6]

list_to_dict(keys, values)

# Python3 code to demonstrate
# conversion of lists to dictionary
# using naive method

# initializing lists
# test_keys = ["Rash", "Kil", "Varsha"]
# test_values = [1, 4, 5]
#
# # Printing original keys-value lists
# print("Original key list is : " + str(test_keys))
# print("Original value list is : " + str(test_values))
#
# # using naive method
# # to convert lists to dictionary
# res = {}
# for key in test_keys:
#     for value in test_values:
#         res[key] = value
#         test_values.remove(value)
#         break
#
# # Printing resultant dictionary
# print("Resultant dictionary is : " + str(res))
