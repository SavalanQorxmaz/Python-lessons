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
    selected = input('Selected student: ')
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
