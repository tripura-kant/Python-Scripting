# This is file 26.py

ages = {
    "Peter": 10,
    "Isabel": 11,
    "Anna": 9,
    "Thomas": 10,
    "Bob": 10,
    "Joseph": 11,
    "Maria": 12,
    "Gabriel": 10,
}
# print one item
print("Get age of peter")
print(ages["Peter"])

## print the whole dictionary
print("Get age of all persons")
for key, value in ages.items():
    print(key, value)
