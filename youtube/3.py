# import random
# number = random.randint(1,10)
#
# print(number)

import sys

if len(sys.argv) < 2:
    print("to few argument")
elif len(sys.argv) > 2:
    print("Too many argument")
else:
    print("hello, my name is ", sys.argv[1])
