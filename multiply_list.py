def multiply_list(num_list):
    multiplier = 2

    for i in num_list:
        multiplier *= i

    return multiplier

print(multiply_list([1, 3, 9]))