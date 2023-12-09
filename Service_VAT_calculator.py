while True:
    
    service_total_price = 0
    service_name = input('Enter service name: ')

    if service_name == 'end':
        break

    start_location = input('Enter start location: ')
    end_location = input('Enter end location: ')
    service_price = float(input('Enter price of service: '))
    vat_price = service_price * 0.20
    total_price = service_price + vat_price
    service_total_price += total_price

print(f'{total_price:.2f}')
