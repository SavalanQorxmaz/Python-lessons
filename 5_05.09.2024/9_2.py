import random
import copy

box = []    # A
i = 1
while i < 6:
    input1 = input(f'Number {i}: ')
    try:
        item = int(input1)
        box.append(item)
        i = i + 1
    except ValueError:
        pass
print(box)
box = [25, 37, 3, 6, 9, 10] # B
sum = 0
for x in box:
    sum += x
print(sum)
sentence = input('Type Sentence: ') # C
words = sentence.split()
print(words)
countries = []   # D
i = 1
while i <= 6:
    country = input('Insert Country: ')
    if country not in countries:
        countries.append(country)
        print(countries)
        i += 1
    else:
        print('This country already have, insert another')
        pass
print('Delete 3 country')
i = 1
while i <=3:
    print(f'Current country list: {countries}')
    selected_country = input('Select country to remove: ')
    if selected_country in countries:
        countries.remove(selected_country)
        i +=1
    else:
        print('No country in the list')
        pass
print(countries)
list1 = [1, 2, 3]   # E
list2 = list1
list3 = list1.copy()
if list2 is list1:
    print('List1 and List2 are same')
if list3 is not list1:
    print('List1 and List3 are not same')
box = []    # F
print(len(box))
names = ['Mahammad', 'Leyla', 'Arzu', 'Ali', 'Xanim', 'Veli']
def find_longest_item(list):
    longest = 0
    longest_item = None
    for item in list:
        if len(item) > longest:
            longest = len(item)
            longest_item = item
    return longest_item
longest_name = find_longest_item(names)
print(longest_name)
box = []    # G
stop = False
i = 1
def find_second_largest_item(list):
    if len(list) < 2:
        return None
    else:
        first = 0
        second = 0
        for item in list:
            if item >= first:
                second = first
                first = item
            elif item > second:
                second = item
        return second
while  not stop:
    print('If you want to finish, write \'stop\' ')
    value = input(f'Number {i}: ')
    if value == 'stop':
        print(value)
        stop = True
        pass
    else:
        try:
            item = int(value)
            box.append(item)
            i = i + 1
        except ValueError:
            print('It is not number')
            pass
print(box)
second_largest = find_second_largest_item(box)
print(second_largest)

print('Task H')     # H
box = []    
stop = False
i = 1
while  not stop:
    print('If you want to finish, write \'stop\' ')
    value = input(f'Number {i}: ')
    if value == 'stop':
        print(value)
        stop = True
        pass
    else:
        try:
            item = int(value)
            box.append(item)
            i = i + 1
        except ValueError:
            print('It is not number')
            pass
sum = 0
mean = 0
length = len(box)
if length > 0:
    for item in box:
        sum += item
    mean = sum / length
    print(box)
    print(mean)
else:
    print('No value in the list')

print('Task I')     # I
box = [] 
stop = False
i = 1
def find_third_smallest_item(list):
    if len(list) < 3:
        return None
    else:
        list.sort()
        return list[2]
while  not stop:
    print('If you want to finish, write \'stop\' ')
    value = input(f'Number {i}: ')
    if value == 'stop':
        print(value)
        stop = True
        pass
    else:
        try:
            item = int(value)
            box.append(item)
            i = i + 1
        except ValueError:
            print('It is not number')
            pass
print(box)
third_smallest = find_third_smallest_item(box)
print(third_smallest)

print('Task J')     # J
colors = input('Enter 3 color with space')
print(f'You enter: {colors}')
colors_list = colors.split()
print(f'Colors array: {colors_list}')
joined_colors = ','.join(colors_list)
print(joined_colors)

print('Task K')     # K
capitals = input('Enter four Capital city with space: ').title()
capitals_list = capitals.split()
if len(capitals_list) > 1:
    print(f'There are many capital cities in the world. For example, {', '.join(capitals_list[:-1])} and {capitals_list[len(capitals_list) - 1]}.')
else:
    print(f'There are many capital cities in the world. For example, {capitals}.')

print('Task L') # L
box = []
stop = False
while not stop:
    print('If you want to finish, enter 0')
    word = input('Enter word: ')
    if word == '0':
        stop = True
        pass
    else:
        box.append(word)
print(f'Entered words: {box}')
box.sort()
print(f'Sorted words: {box}')

print('Task M') # M
box = []    
stop = False
i = 1
while  not stop:
    print('If you want to finish, write \'stop\' ')
    value = input(f'Number {i}: ')
    if value == 'stop':
        print(value)
        stop = True
        pass
    else:
        try:
            item = float(value)
            box.append(item)
            i = i + 1
        except ValueError:
            print('It is not number')
            pass
print(f'Current list: {box}')
box.sort()
box.reverse()
print(f'Descending order: {box}')

print('Task N') # N
box = []
stop = False
while not stop:
    print('If you want to finish, enter 0')
    word = input('Enter word: ')
    if word == '0':
        stop = True
        pass
    else:
        if word in box:
            pass
        else:
            box.append(word)
print(box)

print('Task O') # O
fruits = ['apple', 'banana', 'orange', 'grape', 'apple', 'kiwi']
vegetables = ['onion', 'cucumber', 'brocolli']
basket = fruits + vegetables
print(basket)

print('Task P') # P
my_list = [1,2]
if len(my_list) > 0:    # Method 1
    print(True)
print(bool(my_list))    # Method 2

# - List Comprehension -
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
letters = ['p', 'y', 't', 'h', 'o', 'n']
times = [1, 2, 3, 4, 5]

digits2 = [x**2 for x in digits]
print(digits2)

letters2 = [x.title() for x in letters]
print(letters2)

times_str = [str(x) for x in times]
print(times_str)

numbers = []
for i in range(5):
    numbers.append(random.randrange(-5, 5))
numbers.sort()
second = numbers[1]
print(f'numbers list: {numbers}')
print(f'Second smallest number: {second}')
if second < 0:
    print(True)
else:
    print(False)

numbers = []
for i in range(10):
    numbers.append(random.randrange(0, 100))
print(numbers)
numbers.sort()
print(f'Min: {numbers[0]} Max: {numbers[-1]}')

# - Chat GPT's Homework -

colors = ['white', 'blue', 'red', 'green', 'gray', 'black', 'orange', 'yellow', 'green'] # A
def dublicate_items(list):
    for i in range(len(list)):
        list.insert(2 * i + 1, colors[2 * i])
    return None
print(colors)
dublicate_items(colors)
print(colors)

empty_list1 = []    # B Method 1
print(empty_list1)
empty_list2 = list()    # Method 2
print(empty_list2)

list1 = ['first']   # C
print(list1)
list1.append('second')
print(list1)
list1.insert(len(list1), 'third') 
print(list1)
list1.extend(('fourth',))
print(list1)

my_list = [1, 45, 67, 43, 89]   # D
third = my_list[2]  # Method 1
print(third)
third = my_list[2:3]   # Method 2
print(third)

my_list = [1, 45, 67, 43, 89]   # E
my_list.pop()
print(my_list)

my_list = [1, 45, 67, 43, 89]   # F
my_list.insert(2, 66)
print(my_list)

my_list = [1, 45, 67, 43, 89]   # G
my_list.reverse()
print(my_list)

my_list = [1, 45, 67, 43, 89]   # H
mylist2 = my_list # Shallow copy
mylist2.append('77')
print(f'{my_list= }')
print(f'{mylist2= }')
my_list = [1, 45, 67, 43, 89] 
mylist3 = my_list.copy() # Deep copy
mylist3.append(22)
print(f'{my_list= }')
print(f'{mylist3= }')

my_list = ['a', 'b', 'c', 'a', 'd', 'a']   # I
count = my_list.count('a')
print(count)

list1 = ['a', 'b', 'c', 'a', 'd', 'a'] # J
list2 = [1, 45, 67, 43, 89] 
list3 = list1 + list2   # Method 1
print(list3)
list1.extend(list2) # Method 2
print(list1)

my_list = [1, 45, 67, 43, 89]   # K
my_list.sort()
print(my_list)

my_list = ['x', 'b', 'c', 'x', 'd', 'x']   # L
print(my_list)
my_list.remove('x')
print(my_list)

my_list = ['a', 'b', 'c', 'a', 'd', 'a'] # M
list2 = [1, 45, 67, 43, 89] 
my_list.append('z') # only item
my_list.extend(list2) # any iteration

my_list = ['a', 'b', 'c', 'a', 'd', 'a'] # N
my_list.clear()
print(my_list)

my_list = ['x', 'b', 'c', 'x', 'd', 'x']   # O
first_x = my_list.index('x')
print(first_x)

my_list = ['x', 'b', 'c', 'x', 'd', 'x']   # P
removed_item = my_list.pop(4)
print(removed_item)


'''
Quiz.
1. Which method is used to add an element to the end of a list in Python?
    d) append()

2. What is the purpose of the insert() method for lists in Python?
    c) Add an element at a specific index in the list.

3. Which list method is used to remove and return the last element of a list?
    a) pop() 

4. What does the extend() method do when used on a list in Python?
    b) Adds a new list as elements to the existing list.

5. Which list method is used to reverse the order of elements in a list in Python?
    a) reverse()

6. What does the sort() method do when used on a list in Python?
    c) Sorts the list in ascending order.

7. Which method is used to find the index of the first occurrence of an element in a list?
    a) index()

8. What is the purpose of the pop() method when used on a list in Python?
    b) Removes and returns the last element of the list.

9. How can you count the number of occurrences of a specific element in a list?
    a) Use the count() method.

10. How can you check if a list is empty in Python?
    c) Use the len() function and check if it's equal to zero.

11. Which method is used to copy the elements of one list to another in Python?
    a) copy()

12. How do you remove an element by index from a list in Python?
    b) Use the pop() method with the index as an argument.

13. What does the len() method do when applied to a list?
    c) Returns the number of elements in the list

14. Given the following list, what is the output of min(my_list)?
    my_list = [0, 2, 4, 1, 5]
    result = min(my_list)

    a) 0

15. Given the following list, what is the output of max(my_list)?
    my_list = [0, 2, 4, 1, 5]

    d) 5

16. Which list method can be used to find the number of occurrences 
of a specific element in a list?
    a) count()

17. What is the output of the following code snippet?
    my_list = [1, 2, 3, 4, 5]
    my_list.reverse()
    print(my_list)

    b) [5, 4, 3, 2, 1]

18. What is the output of the following code snippet? 
    my_list = [1, 2, 3] 
    my_list.insert(1, 4) 
    print(my_list)

    b) [1, 4, 2, 3] 

19. Which method is used to remove all elements from a list? 
    a) clear() 

20. What is the output of the following code snippet? 
    my_list = [1, 2, 3, 4, 5] 
    result = sum(my_list) 
    print(result)

    a) 15 

21. What is the output of the following code snippet? 
    my_list = [1, 2, 3, 4, 5] 
    result = my_list.index(3) 
    print(result)

    c) 2 
'''