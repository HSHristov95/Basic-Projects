even_count = 0
odd_count = 0

number = int(input())

for i in range(1, number + 1):
    if i % 2 == 0:
        even_count += 1
    elif i % 2 != 0:
        odd_count += 1

print(f'Even numbers are: {even_count}')
print(f'Odd numbers are: {odd_count}')