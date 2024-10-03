
def print_params(a, b, c):
    print(a, b, c)


params = {'a': 1, 'b': 'строка', 'c': True}
print_params(**params)

values_list = [1, False, "точка"]
values_dict = {'a': 1, 'b': False, 'c': 'точка'}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [37.84, 'бутон']
print_params(*values_list_2, 42)
