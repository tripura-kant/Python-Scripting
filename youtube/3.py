# import random
# number = random.randint(1,10)
#
# print(number)

import sys

if len(sys.argv) < 2:
    sys.exit("to few argument")
elif len(sys.argv) > 2:
    sys.exit("Too many argument")
else:
    print("hello, my name is ", sys.argv[1])
