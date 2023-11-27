while True:
    services = []
    select_type_unit = input('Select service or merch: ')

    if select_type_unit == 'service':
        service_name = input('Enter service name: ')
        services.append(service_name)
        
        if service_name == 'end':
            break

        service_name = input('Enter service name: ')

print(services)