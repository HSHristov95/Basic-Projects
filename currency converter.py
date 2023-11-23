amount = float(input('Enter amount: '))
unit = input('Enter currency: ')

bgn = 0
eur = 0
usd = 0

if unit == 'bgn':
    eur = amount / 1.955642
    usd = amount / 1.790615
    print(f'Your amount in euros is: {eur:.3f}')
    print(f'Your amount in us dollars is: {usd:.3f}')

elif unit == 'eur':
    bgn = amount * 1.955642
    usd = amount * 1.091824
    print(f'Your amount in bulgarian levs is: {bgn:.3f}')
    print(f'Your amount in us dollars is: {usd:.3f}')

elif unit == 'usd':
    bgn = amount * 1.955642
    eur = amount * 0.917017
    print(f'Your amount in bulgarian levs is: {bgn:.3f}')
    print(f'Your amount in euros is: {eur:.3f}')