weight = float(input('Enter your weight: '))
unit = input('Enter the unit: ')

kg = 0
st = 0
lb = 0

if unit == 'kg':
    lb = weight * 2.20462262
    st = weight * 6.35029318
    print(f'Your weight in pounds is: {lb:.1f}')
    print(f'Your weight in stones is: {st:.1f}')

elif unit == 'lb':
    kg = weight * 0.45359237
    st = weight * 0.0714285714
    print(f'Your weight in kilograms is: {kg:.1f}')
    print(f'Your weight in stones is: {st:.1f}')

elif unit == 'st':
    kg = weight * 6.35029318
    lb = weight * 14
    print(f'Your weight in kilograms is: {kg:.1f}')
    print(f'Your weight in stones is: {lb:.1f}')