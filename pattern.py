num = int(input())

for column in range(1, num + 1):
    for row in range(column):
        print('*', end = '')
    print()

for column in range(num - 1, 0, -1):
    for row in range(column):
        print('*', end = '')
    print()