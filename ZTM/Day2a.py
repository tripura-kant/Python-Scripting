'''
for item in (1, 2, 3, 4, 5):
    for x in ('a' ,'b', 'c', 'd', 'e'):
        print(item, x)
'''

user = {
    'name': 'Golean',
    'age': '50',
    'can_swim': False
}

for key, value in user.items():
    print(key, value)

'''

for item in user.values():
    print(item)

for item in user.keys():
    print(item)

'''