select_type_unit = input('Select service or merch: ')

while select_type_unit != 'end':
    services = []

    if select_type_unit == 'service':
        service_name = input('Enter service name: ')
        services.append(service_name)

print(services)