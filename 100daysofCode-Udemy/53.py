import os

f = open('practise.txt', 'w+')
f.write('This is a test string')
f.close()
print('Done')

s = os.getcwd()

print(s)
