import math 

def square_or_not(a):
    sqrt_value = math.sqrt(a)
    return int(sqrt_value) ** 2 == a

num = int(input())

if square_or_not(num):
    print(f'{num} is a perfect square number.')
else:
    print(f'{num} is not a perfect square number.')
