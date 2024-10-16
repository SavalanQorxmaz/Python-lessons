lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 2]

filtered = [*filter(lambda x: x % 2 == 0, lst)]
print(lst)
print(filtered)

my_dict = {
    1: '1',
    3: '3',
    5: '5',
    4: '4',
    2: '2'
}
print([*my_dict.items()])
# my_dict_list = list(my_dict)
# print(my_dict_list)
sorted_dict = dict(map(lambda x: (x[0] * 2, x[1]), [*my_dict.items()]))
print(sorted_dict)