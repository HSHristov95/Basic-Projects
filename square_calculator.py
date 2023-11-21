import math

def square_result(a, b):

    return f'{math.sqrt(a) + math.sqrt(b):.2f}'

num = int(input())
num1 = int(input())

print(square_result(num, num1))
