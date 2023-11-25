import math

def square_number(a):
    sqrt_value = math.sqrt(a)

    return f'{float(sqrt_value):.2f}'

def square_number_1(b):
    sqrt_value_1 = math.sqrt(b)

    return f'{float(sqrt_value_1):.2f}'

def square_add_result(a, b):

    return f'{math.sqrt(a) + math.sqrt(b):.2f}'

def square_subtract_result(a, b):
    return f'{math.sqrt(a) - math.sqrt(b):.2f}'

def square_multiply_result(a, b):
    return f'{math.sqrt(a) * math.sqrt(b):.2f}'

def square_divide_result (a, b):
    return f'{math.sqrt(a) / math.sqrt(b):.2f}'

num1 = int(input())
action = input()
num2 = int(input())

if action == '+':
    print(square_add_result(num1, num2))

if action == '-':
    print(square_subtract_result(num1, num2))

if action == '*':
    print(square_multiply_result(num1, num2))

if action == '/':
    print(square_divide_result(num1,num2))
