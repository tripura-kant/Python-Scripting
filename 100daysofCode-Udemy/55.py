# Modules math and Random Modules

import math
from math import pi

value = 4.5

print(math.floor(value))
print(math.ceil(value))
print(round(value))
print(pi)
print(math.e)
print(math.inf)
print(math.e)
import random

random.seed(33)
x = random.randint(0, 100)
print(x)
print(random.seed(101))

mylist = list(range(0, 20))

print(mylist)

print(random.choice(mylist))

print(random.choices(population=mylist, k=10))
print(random.sample(population=mylist, k=10))
random.shuffle(mylist)
print(mylist)
