import math

def square_number(a):
    sqrt_value = math.sqrt(a)

    return f'{float(sqrt_value):.2f}'

def square_number_1(b):
    sqrt_value_1 = math.sqrt(b)

    return f'{float(sqrt_value_1):.2f}'

def square_result(a, b):

    return f'{math.sqrt(a) + math.sqrt(b):.2f}'

num = int(input())
num1 = int(input())

print(square_result(num, num1))