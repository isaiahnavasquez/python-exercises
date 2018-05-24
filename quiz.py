# 1
def create_group():
    ref = {}
    while True:
        group_name = input('Enter the name of group, \n (enter x to exit): ')
        if group_name == 'x':
            print(ref)
            break
        response = 'y'
        while response == 'y':
            name = input('add a name, \n (enter x to exit): ')
            if name == 'x':
                print(ref)
                break
            else:
                if group_name in ref:
                    ref[group_name].append(name)
                else:
                    ref[group_name] = [name]

# 2
def insert_a_data(data, l):
    return l + [data]

# 3
def odd_numbers(numbers):
    return [x for x in numbers if x % 2 != 0]

# 4
def convert_to_int(numbers):
    return int(''.join([str(x) for x in numbers]))

# 5
def sort_numbers(numbers):
    return sorted(numbers)

# 6
def check_if_empty(l):
    return True if len(l) == 0 else False

# 7
def arrays_to_dict(list_1, list_2):
    return {x:y for x, y in zip(list_1, list_2)}

# 8
def remove_duplicates(l):
    ref = []
    for i in l:
        if i not in ref:
            ref.append(i)
    return ref

# 9
def get_unique(l):
    ref = {}
    for i in l:
        if i not in ref:
            ref[i] = 1
        else:
            ref[i] += 1
    return [i for i, v in zip(ref.keys(), ref.values()) if v == 1]

# 10
def get_index(l, val):
    return l.index(val)

# 11
def find_in_list(l, find):
    output = {}
    for pair in l:
        if find['index'] == pair['index']:
            output = pair
    return output

# 12
def is_existing(l, val):
    return True if val in l else False

# 13
def compare_lists(list_1, list_2):
    return [x for x in list_1 if x not in list_2]

# 14
def remove_non_integer(l):
    return [x for x in l if type(x) == int]

# 15
def display_lists(list_1, list_2):
    for x, y in zip(list_1, list_2):
        print('{} {}'.format(x, y))

# 16
def convert_to_list(string):
    return [x for x in list(string)]

create_group()
