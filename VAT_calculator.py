select_type_unit = input('Select service or merch: ')
services = []
merch = []

while select_type_unit == 'service':
    service_name = input('Enter service name: ')

    if service_name != 'end':
        services.append(service_name)

    if service_name == 'end':
        break

    print(services)

while select_type_unit == 'merch':
    merch_name = input('Enter merch name: ')

    if merch_name != 'end':
        merch.append(merch_name)

    if merch_name == 'end':
        break

    print(merch)