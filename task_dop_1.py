types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
} 

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}
result_dct = {}

def remove_dublicates(dct):
    temp_list = []
    for key, values in dct.items():
        one_value_list = []
        for v in values:
            if v not in temp_list:
                temp_list.append(v)
                one_value_list.append(v)
        result_dct[key] = one_value_list
    return result_dct

def create_joined_data(types, tickets):
    tickets_by_type = {}
    for i in range(len(tickets.keys())):
        tickets_by_type[types[list(types.keys())[i]]] = tickets[list(tickets.keys())[i]]
    print(tickets_by_type)

remove_dublicates(tickets)

create_joined_data(types, result_dct)

