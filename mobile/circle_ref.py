my_dict={}


def create_element(name, el):
    """Creating an element with a str key and int elements to the 'my_dict'"""
    name = str(name)
    el = int(el)
    new_element = {name: el}
    return new_element


def add_element(a_dict, coord):
    """Adding an element with a str key and int elements to the 'my_dict'"""
    new_dict = a_dict
    new_dict.update(coord)
    return new_dict


def check_dict(d_elements, check_val):
    """Now it's time to check d_elements in the d dictionary!"""
    d_elements = {**d_elements}
    print(d_elements)
    check_val = {**check_val}
    print(check_val)
    for i in d_elements:
        # print(i)
        if i in check_val:
            print(i)
            print(i), 'is already in this dictionary!'
        else:
            return check_val


trial = create_element('345', '123')
trial2 = create_element('789', '91011')
trial3 = create_element('121', '313')
trial4 = create_element('345', '123')
added = add_element(trial, trial2)
# print(trial)
check_dict(added, trial2)
check_dict(added, trial2)









