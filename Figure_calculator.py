import math
from math import pi

def calculate_square(a, info):
    area = None
    circumference = None
    result = None

    area = a ** a
    circumference = 4 * a

    if info == 'area':
        result == area
    elif info == 'circumference':
        result == circumference
    else:
        result == 'Wrong!'

    return result

def calculate_circle(r, info):
    area = None
    circumference = None
    result = None

    area = pi * r ** 2
    circumference = r * 2

    if info == 'area':
        result == area
    elif info == 'circumference':
        result == circumference
    else:
        result == 'Wrong!'

    return result

def calculate_rectange(a, b, info):
    area = None
    circumference = None
    result = None

    area = a * b
    circumference = (2 * a) + (2 * b)

    if info == 'area':
        result == area
    elif info == 'circumference':
        result == circumference
    else:
        result == 'Wrong!'

    return result