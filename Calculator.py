def calculate(num1,action,num2):
    result = None
    if action == '+':
        result = num1 + num2

    if action == '-':
        result = num1 - num2

    if action == '*':
        result = num1 * num2

    if action == '/':
        result = num1 / num2

    if action == '%':
        result = num1 % num2

    if action == '**':
        result = num1 ** num2

    return result

num1 = float(input()) 
action = input()
num2 = float(input())

print(calculate(num1,action,num2))