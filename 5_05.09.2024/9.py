# - Lists -

colors = ['white', 'blue', 'red', 'green', 'gray', 'black', 'orange', 'yellow']    # A
countries = ['Azerbaijan', 'Turkiye', 'Ukraina', 'Sweden', 'Hungary', 'Pakistan', 'Italy']    # B
mix_list = ['car', 'home', 'way', 8, 256]   # C
continents = ['Asia', 'Africa', 'North America', 'South America', 'Antarctica', 'Europe', 'Australia']  # D
brands = ['Audi', 'BMW', 'GMC', 'Volvo', 'Ferrari'] # E
data_type_list = [True, 5, 'String', None]  # F
even_negatives = [-12, -10, -8, -6, -4, -2] # G
even_positives = [0, 2, 4, 6, 8, 10, 12]    # H
all_evens = even_negatives + even_positives # I
students = ['Lale', 'Leyla', 'Arzu', 'Ali', 'Xanim', 'Veli']    # J
print(students[0])
numbers = [-12, 9, 19]  # K
print(numbers[1])
print(continents[-1])   # L
print(colors[-2:])  # M
three = [3, 3, 3]   # N
containing_list = [4, 4, 4]
containing_list.extend(three)
nested_list = [1, 2, [3, 4, 5, 6], ['black', 'white', ['orange', 'yellow']]]   # O
print(nested_list[2])
print(nested_list[-1][2])
colors[6] = 'yellowgreen'   # P
print(countries[2:])    # Q
double_data_type_list_1 = data_type_list + data_type_list   # R
# print(double_data_type_list_1)
double_data_type_list_2 = data_type_list * 2
# print(double_data_type_list_2)
friends = ["Kevin", "Karen", "Jim", "Carry"]    # S
friends[-1] = 'Bob'
# print(friends)
empty_list = [] # T

# - Interview Question -
my_list = ["Kevin", "Karen", "Jim", "Carry"]
my_reversed_list = my_list[::-1]
print(my_reversed_list)

# Bonus:
print(colors[:4])
print(continents[::-2])
print(countries[2:])
print(len(brands))