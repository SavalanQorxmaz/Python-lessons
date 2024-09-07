import random

fruits = ["Apple", "Banana", "Orange", "Grape", "Strawberry", "Kiwi", "Cherry"]

# - List Methods -
last_element = fruits[len(fruits)-1]    # A
# print(last_element)
new_fruits = ['Pear', 'Olive']  # B
fruits.extend(new_fruits)
# print(fruits)
removed_fruit = fruits.pop(2)   # C
# print(removed_fruit)
# print(fruits)
fruits.append(removed_fruit)    # D
fruits.insert(2, removed_fruit)
print(fruits.count(removed_fruit))
# print(fruits)
fruit_index = fruits.index('Grape') # E
# print(fruit_index)
fruits.insert(3, 'Avocado') # F
del fruits[2]   # G
# print(fruits)
fruits.pop(0)   # H
# print(fruits)
fruits.append('Blackberry') # I
# print(fruits)
last_index = len(fruits)-1
fruits.pop(last_index)
print(fruits)
reversed_1 = fruits[::-1]   # J
print(reversed_1)
fruits.reverse()
print(fruits)
fruits.sort()   # K
print(fruits)
new_fruits = ["Papaya", "Lime", "Lemon", "Peach"]   # L
fruits.extend(new_fruits)
print(fruits)
copied_list = fruits.copy() # M
# Method 1
# del copied_list[-3:]
# Method 2
copied_list[:] = copied_list[:-3]
print(copied_list)
print(fruits)
occurrence = True if 'Papaya' in fruits else False  # N
# print(occurrence)
fruits.clear()
print(fruits)

# - Variables -
x = 60; y = 70

# - ChatGPT's homework (List Methods) -
box = []    # 1
i = 10
while i <= 50:
    box.append(i)
    i += 10
    print(box)
box_2 = [60, 70, 80]
box.extend(box_2)
print(box)
fruits = ['apple', 'banana', 'orange', 'grape', 'apple', 'kiwi']    # 2
print(fruits)
fruits.insert(2, 'pear')
print(fruits)
fruits.remove('apple')
print(fruits)
numbers = [2, 4, 6, 8, 4, 10, 4, 12, 14]    # 3
count_4 = numbers.count(4)
print(count_4)
first_4 = numbers.index(4)
print(first_4)
my_list =  [5, 23, 78, 12, 98, 56]  # 4
print(my_list)
my_list.sort()
print(my_list)
my_list.reverse()
print(my_list)
colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple'] # 5
print(colors)
colors_2 = colors[:3]
print(colors_2)
colors_3 = colors[-3:]
print(colors_3)
colors_4 = colors_2 + colors_3
print(colors_4)


