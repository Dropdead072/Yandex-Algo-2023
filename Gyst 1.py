def list_normalization(a):
    reader.close()
    in_string = a.split(' ')
    sorted_set = set(''.join(in_string))
    element_list = list(sorted_set)
    element_list.sort()
    if element_list[0] == '\n':
        element_list.pop(0)
    return element_list


def dict_forming(element_list):
    element_dict = {item: 0 for item in element_list}
    return element_dict


def counting(a, element_dict):
    for element in a:
        if element != '\n' and element != ' ':
            element_dict[element] += 1
        else:
            continue
    return element_dict


def plotting(element_dict_2, element_list):
    current_max = element_dict_2[max(element_dict_2, key=lambda x: element_dict_2[x])]
    while current_max > 0:
        for i in element_list:
            if element_dict_2[i] >= current_max:
                print('#', end='')
            else:
                print(' ', end='')
        print('\n', end='')
        current_max -= 1


reader = open('Gyst_1.txt', 'r')
a = reader.read()
element_list = list_normalization(a)
element_dict = dict_forming(element_list)
length = len(element_list)
element_dict_2 = counting(a, element_dict)
plotting(element_dict_2, element_list)
print(*element_list, sep='')
