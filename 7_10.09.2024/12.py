from math import pi

# - Dictionaries -

personal_data = {   # A
    'firstname': 'Savalan',
    'lastname': 'Qorxmaz',
    'age':35,
    'gender': 'male'
}

fruits = {  # B
    'apple': 200,
    'pear': 100,
    'banana': 100,
    'orange': 20,
}

fruits['banana'] = 120  # C

students_math_grade = {     # D
    'Ali': 8,
    'Jack': 6,
    'Bob': 9,
    'Mark':6,
    'Michicle': 7
}

students_math_grade['Mark'] = 9     # E
print(students_math_grade)

favorite_car = {       # F
    'brand': 'BMW',
    'manufacturing_contry': 'Germany',
    'tires': 19,
    'color': 'White',
    'year': 2024
}

continents = {      # G
    'asia': ['China', 'Korea', 'Japan', 'Singapur'],
    'europa': ['England', 'Hungary', 'Spain', 'Finland'],
    'america': ['USA', 'Kanada', 'Mexico', 'Brasil'],
    'africa': ['Somali', 'Chad', 'Kongo', 'Nigeria'],
    'australia': ['Australia', 'New Zeland', 'Oceania'],
    'antarctida': []
}

english_dict = {        # H
    'bad': 'of poor quality or a low standard',
    'good': 'to be desired or approved of',
    'excellent': 'extremely good; outstanding',
    'poor': 'lacking sufficient money to live at a \
        standard considered comfortable or normal in a society',
    'rich': 'having a great deal of money or assets; wealthy',
}
print(english_dict)
length_dict = len(english_dict)
print(f'Dictionary length is: {length_dict}')

'''J
As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, 
dictionaries are unordered.

K
ordered 
changeable
No duplicate members.

L
Only string objects or data types can be represented as keys in dictionaries.
'''

students_keys = students_math_grade.keys()  # M
print(students_keys)
students_math_grade_values = students_math_grade.values()   # N
print(students_math_grade_values)
student_items  = students_math_grade.items()    # O
print(f'Students items are: {student_items}')

car = {     # P
    "model": "Camaro",
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "brand": "Chevrolet",
    "color": "red",
}
print(car)
# Output: {'model': 'Mustang', 'brand': 'Chevrolet', 'year': 1964, 'color': 'red'}
# not allow duplicates.
car['color'] = 'blue'   # Q
car['manufacturing_contry'] = 'USA'     # R

fstring_method = f'Firstname: {personal_data['firstname']}\nLastname : {personal_data   ['lastname']}\nAge: {personal_data['age']}\nGender: {personal_data['gender']}' # S
print(fstring_method)
format_method = 'Firstname: {}\n Lastname : {}\n Age: {}\nGender: {}'.format(personal_data['firstname'], personal_data['lastname'], personal_data['age'], personal_data['gender'])
print(format_method)
s_method = 'Firstname: %s\nLastname : %s\n Age: %s\nGender: %s' % (personal_data['firstname'], personal_data['lastname'], personal_data['age'], personal_data['gender'])
print(s_method)

empty_dict = dict()     # T
length_empty_dict = len(empty_dict)
print(f'Empty dictionary length is: {length_empty_dict}')
empty_dict2 = {}
print(type(empty_dict2))
grades = {      # U
    'Alice': 85,
    'Bob': 90,
    'Charlie': 78,
    'David': 92,
    'Emily': 88
}

student = input('Selected student: ').lower().title()
while student not in grades:
    print('No student as this name')
    student = input('Selected student: ').lower().title()
grades[student] += 7
print(grades)

word_definitions = {        # V
    'apple': 'a round fruit with red or green skin and crisp flesh',
    'computer': 'an electronic device for processing and storing data',
    'book': 'a written or printed work consisting of pages',
    'ocean': 'a large body of saltwater that covers most of the Earth\'s surface',
    'mountain': 'a large natural elevation of the Earth\'s surface'
}
selected = input('Selected item: ')
while selected not in word_definitions:
    print('No student as this name')
    selected = input('Selected item: ')
length = len(word_definitions[selected])
print(f'Selected item length is: {length}')

# - ChatGPT's homework (Dictionaries) -

student_scores = {      # A
    'Alice': 85,
    'Bob': 92,
    'Eve': 78,
    'Charlie': 95
}
print(student_scores)
student_scores.update({'David': 88})    # B
print(student_scores)
student_scores['Eve'] = 82  # C
student_scores.pop('Bob')   # D

my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}  # E
key = input('Enter key: ')
if key not in my_dict.keys():
    print('Not found')
else:
    print(f'{key} is {my_dict[key]}')

new_dict = {}
key  = input('Enter key: ')
value = input('Enter value: ')
new_dict.update({key: value})
print(new_dict)

# - I/O -
print('Rectangle perimeter')    # A
side1 = int(input('Side 1: '))
side2 = int(input('Side 2: '))
perimeter = (side1 + side2) * 2
print(f'perimeter is: {perimeter}')
print('Rectangle area')    # B
side1 = int(input('Side 1: '))
side2 = int(input('Side 2: '))
area = side1 * side2
print(f'Area is: {area}')
print('Square perimeter')    # C
side = int(input('Side: '))
perimeter = side * 4
print(f'Area is: {perimeter}')
print('Square area')    # D
side = int(input('Side: '))
area = side**2
print(f'Area is: {area}')
print('Circle area')    # E
radius = int(input('Radius: '))
area = pi * radius**2
print(f'Circle area is: {area}')
print('Circle perimeter')    # F
radius = int(input('Radius: '))
length = 2 * pi * radius
print(f'Circle length is: {length}')

# Quiz.
'''
1. What is a dictionary in Python?
    b) A collection of key-value pairs

2. How do you create an empty dictionary in Python?
    a) my_dict = {}
    b) my_dict = dict()

3. How do you access a value in a dictionary using its key?
    a) my_dict.get(key)
    b) my_dict[key]
    
4. Can a dictionary have duplicate keys?
    b) No
    
5. How do you add a new key-value pair to an existing dictionary?
    b) my_dict[key] = value
    
6. How do you remove a key-value pair from a dictionary?
    c) del my_dict[key]
    d) my_dict.pop(key)
    
7. Which method returns a list of all the keys in a dictionary?
    a) my_dict.keys()

8. How do you check if a key is in a dictionary?
    a) key in my_dict

9. What happens if you try to access a key in a dictionary that doesn't exist?
    a) It raises a KeyError

10. Which dictionary method is used to retrieve the value associated with a key, 
and if the key does not exist, return a default value instead of raising an error?
    a) get(key, default)

11. Which dictionary method is used to remove all key-value pairs from the dictionary?
    a) clear()

12. Which dictionary method returns a new dictionary with keys from the given sequence and 
values set to a specified value?
    a) fromkeys(seq, value)

13. Which dictionary method returns a list of tuples, each tuple containing a key-value pair 
from the dictionary?
    a) items()

14. Which dictionary method returns a list of all the values in the dictionary?
    a) values()

15. Which dictionary method returns and removes an element with a specified key?
    a) pop(key)
    
16. Which dictionary method returns a shallow copy of the dictionary?
    a) copy() ?????????????????

17. Which dictionary method is used to update the dictionary with key-value pairs 
from another dictionary or from an iterable of key-value pairs?
    a) update(iterable)

18. Which dictionary method returns the value for a specified key and removes the 
key-value pair from the dictionary?
    a) popitem()
    
19. What will be the output of this code:
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    print(my_dict.get('b'))

    b) 2
        
20. What will be the output of this code:
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    my_dict['d'] = 4
    print(my_dict)
    
    b) {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    
21. What will be the output of this code:
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    my_dict.pop('b')
    print(my_dict)

    a) {'a': 1, 'c': 3}

22. What will be the output of this code:
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    print(list(my_dict.items()))

    a) [('a', 1), ('b', 2), ('c', 3)]
    
23. What will be the output of this code:
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    my_dict.update({'b': 5, 'd': 4})
    print(my_dict)

    b) {'a': 1, 'b': 5, 'c': 3, 'd': 4}

24. What is the main difference between the pop() and popitem() methods in Python dictionaries?
    a) pop() allows you to remove a specific key-value pair by providing the key, while popitem() 
    removes and returns an arbitrary key-value pair. before 3.7
'''
