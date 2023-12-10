eu_countries_list = ['Austria', 'Belgium', 'Bulgaria', 'Cyprus', 'Czech Republic', 'Denmark',
'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Ireland', 'Italy', 'Latvia',
'Lithuania', 'Luxembourg', 'Malta', 'Netherlands', 'Poland', 'Portugal', 'Romania' , 'Slovakia',
'Slovenia', 'Spain', 'Sweden']

total_price = 0
service_total_price = 0

while True:
    
    service_name = input('Enter service name: ')

    if service_name == 'end':
        break

    start_location = input('Enter start location: ')
    end_location = input('Enter end location: ')
    service_price = float(input('Enter price of service: '))
    if start_location in eu_countries_list:
        vat_price = service_price * 0.20
        total_price = service_price + vat_price
        service_total_price += total_price
        print(f'{total_price:.2f}')
    else:
        break

print(f'{service_total_price:.2f}')
