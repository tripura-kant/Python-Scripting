# This is file 12.py

import math


def calculateSinCosTan(x):
    sine = math.sin(x)
    cos = math.cos(x)
    tan = math.tan(x)
    return [sine, cos, tan]


print(calculateSinCosTan(30))
