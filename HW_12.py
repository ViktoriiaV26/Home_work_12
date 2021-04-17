import json


def make_dict():
    with open('HW.json', 'r') as json_data:
        date_ = json.load(json_data)
    return date_


def dict_sort(date_):
    employee = date_['employee']
    my_dict_ = {}
    for person in employee:
        first_name = person.get('firstName')
        last_name = person.get('lastName')
        fio = f"{first_name} {last_name}"
        ints = []
        strings = []
        floats = []
        nons = []
        bool_ = []
        for pers_key, pers_value in person.items():
            if type(pers_value) == int:
                ints.append(pers_value)
            elif type(pers_value) == str:
                strings.append(pers_value)
            elif type(pers_value) == float:
                floats.append(pers_value)
            elif type(pers_value) is None:
                nons.append(pers_value)
            elif type(pers_value) == bool:
                bool_.append(pers_value)
        my_dict2 = {'int': ints, 'string': strings, 'float': floats, 'None': nons, 'bool': bool_}
        my_dict3 = {fio: my_dict2}
        my_dict_.update(my_dict3)
        date_.update({'employee': my_dict_})
    return date_


def save_sorted_dict(date_):
    with open('HW_result.json', 'w') as file:
        json.dump(date_, file, indent=3)


def main():
    save_sorted_dict(dict_sort(make_dict()))


main()
