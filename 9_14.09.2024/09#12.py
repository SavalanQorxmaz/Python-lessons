import random
# Instructions: Write Python code for each of the following tasks. 
# Make sure to use if statements appropriately to achieve the desired outcomes. 
# If appropriate, comment your code to explain each step.

# - If Statements -

'''A. Create any variable with Boolean value. Print 'My variable evaluates to True'
if this variable is 'True', otherwise print 'My variable evaluates to False'.'''

is_true = True
if is_true:
    print('My variable evaluates to True')
else:
    print('My variable evaluates to False')

'''B. Create a variable named 'temperature'. Make it equal to any degree. Check:
1. If temperature is under 10 degrees, print 'It\'s cold outside, take a scarf.'.
2. If temperature is in interval from 10 to 24 degrees (both included), print 
'It\'s a nice weather. Let\'s go for a walk.'.
3. If temperature is above 24 degrees, print 'It\'s quite hot, I need an AC.'.'''

temperature = 25
if temperature < 10:
    print('It\'s cold outside, take a scarf.')
elif 10 <= temperature <= 24:
    print('It\'s a nice weather. Let\'s go for a walk.')
else:
    print('It\'s quite hot, I need an AC.')

'''C. Create a variable named 'age'. Make it equal your age. Check:
1. If it's under 18, print 'I am not eligible for voting :('
2.If you are 18 or older, print 'I am eligible for voting!'''

age = 35
if age < 18:
    print('I am not eligible for voting :(')
else:
    print('I am eligible for voting!')

'''D. Create variables 'a' and 'b'. Make them equal 15 and 20 correspondingly.
Check if their sum gives less than 40, print their sum and add 'It\'s less than 40.'.
Otherwise, print their sum and add 'It makes 40 or more than 40.'.'''

a, b = 15, 20
sum = a + b
if sum < 40:
    print(f'Sum: {sum} It\'s less than 40.')
else:
    print(f'Sum: {sum} It makes 40 or more than 40.')

'''E. Create a list with 4 students (make it contain their names). Check if the 
length of that list is less than 5, add new student to that list.'''

students = ['Lale', 'Leyla', 'Ali', 'Murad']
if len(students) < 5:
    students.append('Senan')

'''F. Create four variables (a, b, c, d) with numeric (int & float) values.
Write the logical expression to check if 'a' is greater than 'b' and 'c' is greater
than 'd'.'''

a, b, c, d = (3, 5.8, -23, 96)
if(a > b) and (c > d):
    print(True)
else:
    print(False)

'''G. Write a program to check whether a number accepted from user is divisible by 2
and 3 both.
'''
# print('divisible by 2 and 3')
# user_input = input('Number: ')
# number = 0
# is_allright = False
# while not is_allright:  # Check if input is number
#     try:
#         if int(user_input):
#             number = int(user_input)
#             is_allright = True

#     except ValueError:
#         print('Only number!')
#         user_input = input('Number: ')
#         pass
# print(number)
# if(number % 6 == 0):    # Method 1
#     print(f'{number} divide 2 and 3')
# else:
#     print(f'{number} does not divide 2 and 3')
# if(number % 2 == 0 and number % 3 == 0):    # Method 2
#     print(f'{number} divide 2 and 3')
# else:
#     print(f'{number} doesn\'t divide 2 and 3')

'''H. Write a program that finds the largest number out of three numbers accepted from user.
'''
# print('Largest number find')
# numbers = []
# length = len(numbers) 
# print('Add  3 numbers, click Enter after every number')
# while len(numbers) < 3:
#     user_input = input('Enter number: ')
#     try:
#         if int(user_input):
#             numbers.append(int(user_input))
#             pass
#     except ValueError:
#         print('Only number!')
#         pass
    
# print(numbers)
# numbers.sort()
# print(f'Largest is: {numbers[-1]}')

'''I. Write a program that gets any input from user. It should print 'Lower job!' if all
characters in user's input are lowercase, otherwise print 'Upper job!'.
'''
# user_input = input('Any word or sentence: ')
# if user_input.islower():
#     print('Lower job!')
# else:
#     print('Upper job!')

'''J. Write a program to check whether a number entered by user is three digit number or not.
'''
# print('Number three digit or')
# user_input = input('Number: ')
# number = None
# while number is None:  
#     try:
#         if int(user_input):
#             number = int(user_input)

#     except ValueError:
#         print('Only number!')
#         user_input = input('Number: ')
#         pass
#     div_number = number // 100
# if 0 < div_number < 10:
#     print(f'{number} is three digit number')
# else:
#     print(f'{number} is not three digit number')

'''K. Accept the temperature in degree Celcius of water and check whether it's boiling or
not (boiling point of water is 100 degree Celcius).
'''
# temperature = None
# user_input = input('Enter temperture: ')
# try:
#     if int(user_input):
#         temperature = int(user_input)
#         if(temperature > 100):
#              print('it\'s boiling')
#         else:
#              print('it\'s not boiling')
# except ValueError:
#     print('It is not temperature')
#     pass

'''L. Accept the IQ of 3 people and display the highest one.
'''
# print('IQ of 3 people and display the highest one')
# persons = {
#     'Lale': 0,
#     'Leyla': 0,
#     'Leman': 0
#     }
# for x in persons:
#     print(f'{x}:', end='   ')
#     persons.update({x: input()})
# print(persons)
# values_list = list(persons.values())
# values_list.sort()
# print(values_list)
# for person in persons:
#     if persons[person] == values_list[-1]:
#         print(f'{person} {persons[person]} IQ highest')
#         break

'''M. Write a program to check whether a character accepted from user is vowel or not.
'''
# print('Character accepted from user is vowel or not')
# vowel_chars = ('a', 'e', 'i', 'o', 'u')
# value = input('character: ')
# if value.strip()[-1] in vowel_chars:
#     print(True)
# else:
#     print(False)


'''N. Accept the following from the user and calculate the percentage of class attendance:
1. Total number of class days
2. Total number of days for absence
'''

# class_dict = {
#     'class_days': 0,
#     'absence': 0
#     }
# for x in class_dict.keys():
    
#     is_int = False
#     while is_int == False:
#         print(f'{x}:', end='   ')
#         try:
#             days = int(input())
#             class_dict.update({x: days})
#             is_int = True
#         except ValueError:
#             print('Only Number')
#             pass
# attendance_percentage = 100 / class_dict['class_days'] * (class_dict['class_days'] - class_dict['absence'])
# print(f'percentage of class attendance: {attendance_percentage:.1f} %')


'''O. Accept the percentage from the user and display the grade according to the following
criterias:
1. Below 25 - D
2. 25 to 45 - C
3. 45 to 50 - B
4. 50 to 60 - B+
5. 60 to 80 - A
6. Above 80 - A+
'''



# - Dictionary Methods -
'''A. Create a nested dictionary. Get any inner value using multiple key-indexing.
'''
print('Nested dictionary')
my_dict = {
    'city': 'baku',
    'language': 'AZ',
    'car': {
        'model': 'audi',
        'country':'Germany',
        'year': 2024,
        'e-tron': True
    },
    
}
country = my_dict['car']['country']
print(country)

'''B. Create a dictionary with your personal data (name, surname, age, family status,
gender). Ask user for any key in your dictionary. Print the value of the given
key from the dictionary. Try to ask all keys.
'''
# person = {
#     'name': 'Savalan',
#     'surname': 'Qorxmaz',
#     'age': 35,
#     'family_status': 'single'
# }
# *rest, b = tuple(person.keys())
# print(f'Enter {', '.join(rest)} or {b}')
# user_input = input('key: ')
# if user_input in person.keys():
#     print(person[user_input])
# else:
#     print('There are no key')

'''C. Create a dictionary with stock data of clothes (cloth name + amount). Let 
the user choose any of keys and add some count to it.
'''
print('data of clothes')
clothes = {
    'shoes': 100,
    'jacket': 80,
    'shirt': 50
}
# new_clothe = input('Add new one')
# clothes.update({new_clothe: 200})
# print(clothes)

'''D. Copy any dictionary from previous tasks. Print it.
'''
print('Copy dictionary')
clothes2 = clothes.copy()
print(clothes2)

'''E. Clear the dictionary from Task D. Print the length of this dictionary.
'''
clothes2.clear()
print(clothes2)

'''F. Create an empty dictionary. Let the user add data to it (key & value). Choose
any topic (books, cars, info, items, grades...) and let the user fill it with
minimum 4 key-value pairs.
'''
print('user add data to dictionary (key & value).')
# new_dict = {}
# stop = ''
# while stop != 'stop':
#     key = input('Add key: ')
#     value = input('Add value: ')
#     stop =  input('If yo want to cancel, write stop, else what you want): ')
#     new_dict.update({key: value})
# print(new_dict)

'''G. You have the following dictionary:
car = {
    "brand": "Chevrolet",
    "model": "Camaro",
    "year": 2017
}

Create a 'not_found_message' variable. Make it equal appropriate "not found" message.
Try to get 'year's and 'color's values from the 'car'. Set the default value to 
our "not found" message.
'''
car = {
    "brand": "Chevrolet",
    "model": "Camaro",
    "year": 2017
}
not_found_message = 'not found'
year = car.get('year', not_found_message)
color = car.get('color', not_found_message)
print(f'car\'s year: {year}, car\'s color: {color}')

'''H. Print the first 6 keys from the following dictionary (hint: you should use 
'list()' method to convert dict_keys to list and indexing to get the appropriate
portion of data):
countries_capitals = {
    "USA": "Washington, D.C.",
    "Canada": "Ottawa",
    "United Kingdom": "London",
    "France": "Paris",
    "Germany": "Berlin",
    "Japan": "Tokyo",
    "Australia": "Canberra",
    "Brazil": "Brasília",
    "India": "New Delhi",
    "South Africa": "Pretoria",
}
'''
countries_capitals = {
    "USA": "Washington, D.C.",
    "Canada": "Ottawa",
    "United Kingdom": "London",
    "France": "Paris",
    "Germany": "Berlin",
    "Japan": "Tokyo",
    "Australia": "Canberra",
    "Brazil": "Brasília",
    "India": "New Delhi",
    "South Africa": "Pretoria",
}
dict_keys = list(countries_capitals.keys())

print(f'First 6 key: {[dict_keys[i] for i in range(len(dict_keys)) if i<6]}')

'''I. You have the following dictionary:
programming_languages = {
    "Python": {
        "designed_by": "Guido van Rossum",
        "first_appeared": 1991,
        "paradigm": "Multi-paradigm",
        "typing": "Dynamic",
        "popularity": "High"
    },
    "JavaScript": {
        "designed_by": "Brendan Eich",
        "first_appeared": 1995,
        "paradigm": "Multi-paradigm",
        "typing": "Dynamic",
        "popularity": "Very High"
    },
    "Java": {
        "designed_by": "James Gosling",
        "first_appeared": 1995,
        "paradigm": "Object-oriented",
        "typing": "Static",
        "popularity": "High"
    },
    "C++": {
        "designed_by": "Bjarne Stroustrup",
        "first_appeared": 1985,
        "paradigm": "Multi-paradigm",
        "typing": "Static",
        "popularity": "Moderate"
    }
}

Using in f-strings print the year Python was appeared value.
'''
programming_languages = {
    "Python": {
        "designed_by": "Guido van Rossum",
        "first_appeared": 1991,
        "paradigm": "Multi-paradigm",
        "typing": "Dynamic",
        "popularity": "High"
    },
    "JavaScript": {
        "designed_by": "Brendan Eich",
        "first_appeared": 1995,
        "paradigm": "Multi-paradigm",
        "typing": "Dynamic",
        "popularity": "Very High"
    },
    "Java": {
        "designed_by": "James Gosling",
        "first_appeared": 1995,
        "paradigm": "Object-oriented",
        "typing": "Static",
        "popularity": "High"
    },
    "C++": {
        "designed_by": "Bjarne Stroustrup",
        "first_appeared": 1985,
        "paradigm": "Multi-paradigm",
        "typing": "Static",
        "popularity": "Moderate"
    }
}
print(f'Python year: {programming_languages['Python']['first_appeared']}')

'''J. You have the following code snippet:
tasks = {
    "Alice": ["Buy groceries", "Finish report", "Call the doctor"],
    "Bob": ["Walk the dog", "Pay bills", "Read a chapter"]
}

selected_person = "Alice"
new_task = "Go to the gym"

Add the new task to the selected person's tasks. Print the tasks & length of tasks 
before and after edition.
'''
tasks = {
    "Alice": ["Buy groceries", "Finish report", "Call the doctor"],
    "Bob": ["Walk the dog", "Pay bills", "Read a chapter"]
}
selected_person = "Alice"
new_task = "Go to the gym"
print(f'Before tasks length: {len(tasks)}')
values = tasks['Alice']
values.append(new_task)
tasks.update({selected_person : values})
print(tasks)
print(f'After tasks length: {len(tasks)}')

'''K. There is a dictionary method that helps to create a dictionary with a collection
of keys and apply a default value to that key. Using that method create a dictionary
with all values equal to the '[0, 4, 8, 12, 16, 20]' list and keys should only be
the numbers from 0 to 4, so your dictionary should look like:
digits = [1, 2, 3, 4, 5]

my_dict = {
    0: [0, 4, 8, 12, 16, 20],
    1: [0, 4, 8, 12, 16, 20],
    2: [0, 4, 8, 12, 16, 20],
    3: [0, 4, 8, 12, 16, 20],
    4: [0, 4, 8, 12, 16, 20],
}

You should use list comprehension in this task.

Then you should print some portion from the list values of a dictionary. The
portion size depends on a key you are using to index the list.
'''

digits = [0, 1, 2, 3, 4, 5]
value = [x*4 for x in digits]
my_dict = dict.fromkeys(digits, value)
print(my_dict)

'''L. Print all items, values, keys from 'programming_languages' dictionary.
'''
item_list = programming_languages.items()
print(item_list)
keys_list = programming_languages.keys()
print(keys_list)
value_list = programming_languages.values()
print(value_list)
'''M. Remove 'Java' from 'programming_languages' dictionary & get its value. Print it.
'''
print('Remove Java')
removed_language = programming_languages.pop('Java')
print(removed_language)

'''N. Remove the last item from the following dictionary and print it:
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
'''
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
last_item = car.popitem()
print(last_item)

'''O. Expand 'programming_languages' dictionary with the following data:
language_to_add = {
    "PHP": {
        "designed_by": "Rasmus Lerdorf",
        "first_appeared": 1995,
        "paradigm": "Server-side scripting",
        "typing": "Dynamic",
        "popularity": "Moderate"
    }
}
'''
language_to_add = {
    "PHP": {
        "designed_by": "Rasmus Lerdorf",
        "first_appeared": 1995,
        "paradigm": "Server-side scripting",
        "typing": "Dynamic",
        "popularity": "Moderate"
    }
}

programming_languages.update(language_to_add)
print(programming_languages)

'''P. Use 'setdefault' method on any dictionary.
'''
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

color = car.setdefault("color", "white")
print(color)
print(car)

'''Q. Which Data Types can be represented as values of any dictionary?
'''
# All data types

'''R. In the following example:
data = {
    "Python3.x": {
        "Wep Development", "Machine Learning", "Penetration Testing", "Game Development"
    }
}

It's giving an error if you try to get 'Python2.x' in this way:
data["Python2.x"]
Edit this code so it doesn't return an error.
'''
data = {
    "Python3.x": {
        "Wep Development", "Machine Learning", "Penetration Testing", "Game Development"
    }
}
python2 = data.get('Python2.x')
print(python2)

# - Chat GPT's Homework -
'''Task 1.
Create an empty dictionary called student_info.
Add the following key-value pairs to the dictionary:
"name": "John Doe"
"age": 20
"major": "Computer Science"
'''
student_info = {}
student_info.update({'name': 'John Doe', 'age': 20, 'major': 'Computer Science'})
print(student_info)

'''Task 2.
Print the value associated with the key "name" from the student_info dictionary.
Change the value of the "age" key to 21.
Add a new key-value pair: "gender": "Male".
'''
name = student_info.get('name')
print(name)
student_info['age'] = 21
student_info.update({'gender': 'Male'})
print(student_info)

'''Task 3.
Create a new dictionary called grades with the following data:
"math": 85
"english": 92
"history": 78
Use the update method to add the key-value pairs from the grades dictionary into the student_info dictionary.
'''
grades = {
    'math': 85,
    'english': 92,
    'history': 78
}
student_info.update({'grades': grades})
print(student_info)


'''Task 4.
Remove the "history" key from the grades dictionary using the pop method, and print the value that was removed.
Remove the "major" key from the student_info dictionary using the del statement.
'''
removed_grade = grades.pop('history')
print(removed_grade)
del student_info['major']
print(student_info)


'''Task 5: Basic If-Else Statements
Write a Python program that does the following:
Takes an integer input from the user.
Checks if the input is greater than 10.
If it is, prints "The number is greater than 10."
If it's not, prints "The number is not greater than 10."
'''

# ready = False
# while not ready:
#     number_str = input('Chek number is greater than 10: ')
#     try:
#         if int(number_str) or int(number_str) == 0:
#             number = int(number_str)
#             if number <= 10:
#                 print('The number is not greater than 10')
#             else:
#                 print('The number is greater than 10')
#         ready = True   
#     except ValueError:
#         print('Only number!')
#         pass
    

'''Task 6: Multiple Conditions
Write a Python program that:
Takes two integer inputs from the user.
Checks if both numbers are even (divisible by 2).
If both are even, prints "Both numbers are even."
If at least one is not even, prints "At least one number is not even."
'''
# print('Check if number even')
# even_dict = {}
# for x in range(2):
#     ready = False
#     while not ready:
#         number_str = input('Number: ')
#         try:
#             if int(number_str) or int(number_str) == 0:
#                 number = int(number_str)
#                 if number % 2 == 0:
#                     even_dict.update({number_str: True})
#                 else:
#                     even_dict.update({number_str: False})
#             ready = True   
#         except ValueError:
#             print('Only number!')
#             pass
# multiple = True
# for x in even_dict.values():
#    multiple = multiple and x
# print(even_dict)
# print(multiple)
# if multiple:
#     print('Yes')
# else:
#     print('No')

'''Task 7: Grade Calculator
Write a Python program that:
Takes a numerical score as input from the user (0 to 100).
Uses if-elif-else statements to determine the corresponding letter grade based on the following scale:
A: 90-100
B: 80-89
C: 70-79
D: 60-69
F: 0-59
Prints the calculated letter grade.
'''
# F = [x for x in range(61)]
# D = [x + 61 for x in (range(10))]
# C = [x + 71 for x in (range(10))]
# B = [x + 81 for x in (range(10))]
# A = [x + 91 for x in (range(10))]
# score = int(input('Your score: '))
# if score in A:
#     print('A')
# elif score in B:
#     print('B')
# elif score in C:
#     print('C')
# elif score in D:
#     print('D')
# elif score in F:
#     print('F')

'''Task 8: Leap Year Checker
Write a Python program that:
Takes a year as input from the user.
Checks if the year is a leap year or not.
A leap year is divisible by 4, but not divisible by 100 unless it's also divisible by 400.
Prints "Leap year" or "Not a leap year" accordingly.
'''
# print('Leap Year Checker')
# year = int(input('Year: '))
# if year % 400 == 0:
#     print('Leap year')
# else:
#     print('Not a leap year')

'''Task 9: Temperature Converter
Write a Python program that:
Takes a temperature in Celsius as input from the user.
Converts it to Fahrenheit using the formula: Fahrenheit = (Celsius * 9/5) + 32.
Prints the temperature in Fahrenheit.
'''
# print('Temperature Converter')
# temperature = int(input('Enter temperature: '))
# fahrenheit = temperature * 9 / 5  + 32
# print(f'Temperature: {fahrenheit} Fa')

'''Task 10: Number Comparison
Write a Python program that:
Takes three integer inputs from the user.
Determines and prints the largest of the three numbers using if-else statements.
'''
# a = int(input('a= '))
# b = int(input('b= '))
# c = int(input('c= '))
# if a >= b and a >= c:
#     print(f'Max = {a}')
# elif b >= a and b >= c:
#     print(f'Max = {b}')
# elif c >= a and c >= b:
#     print(f'Max = {c}')


'''Task 11: Positive or Negative
Write a Python program that:
Takes an integer as input from the user.
Checks if the number is positive, negative, or zero.
Prints "Positive," "Negative," or "Zero" accordingly.
'''
# print('Positive or Negative')
# number = int(input('Number: '))
# if number > 0:
#     print('Positive')
# elif number < 0:
#     print('Negative')
# else:
#     print('Zero')

'''Task 12: Eligibility Checker
Write a Python program that:
Takes the age and citizenship status (True for U.S. citizen, False for non-U.S. citizen) as input from the user.
Checks if the person is eligible to vote in the U.S. based on the following conditions:
Must be at least 18 years old.
Must be a U.S. citizen.
Prints "You are eligible to vote" or "You are not eligible to vote" accordingly.
'''
# print('Eligibility Checker')
# citizenship = int(input('1 for U.S. citizen, 0 for non-U.S. citizen: '))
# age = int(input('Age: '))
# if age > 18 and citizenship:
#     print('You are eligible to vote" or "You are not eligible to vote')
# else:
#     print('False')

'''Task 13: Password Strength Checker
Write a Python program that:
Takes a password as input from the user.
Checks the strength of the password based on the following criteria:
At least 8 characters long.
Contains both uppercase and lowercase letters.
Contains at least one digit (0-9).
Prints "Strong password" or "Weak password" accordingly.
'''
# print('Password Strength Checker')
# password = input('Check password: ')
# if len(password) > 7 and not password.islower() and not password.isupper() \
#     and not password.isalpha() and not password.isdigit():
#     print('Strong password')
# else:
#     print('Weak password')

'''Task 14: Rock-Paper-Scissors Game
Write a Python program that:
Implements a simple text-based rock-paper-scissors game.
Takes the player's choice as input (rock, paper, or scissors).
Generates a random choice for the computer.
Determines the winner based on the game rules.
Prints the result of the game (win, lose, or tie) and the computer's choice.
'''
# print('Rock-Paper-Scissors Game')
# values = ['rock', 'paper', 'scissors']
# selected = random.choice(values)
# user_input = input('Your choice: ').strip().lower()
# if user_input not  in values:
#     print('Wrong choice')
# else:
#     if user_input == selected:
#         print('Win')
#     else:
#         print('Lose')  

'''- Comments -
A. One-line comment in any random three places of your code, if it's appropriate.
B. Multi-line comment anywhere in your code, if it's appropriate.'''



# Quiz. (If-Statements)
# 1. What is the keyword used to define an 'if' statement in Python?
#     a) if

# 2. How do you write an if statement in Python?
#     a) if condition:

# 3. In Python, what is the symbol for 'not equal to' in an if statement?
#     b) !=

# 4. In Python, what is the purpose of the 'elif' statement?
#     c) It is executed if the 'if' condition is False.

# 5. What will be the output of the following Python code?
#     if 10 > 5:
#         print("10 is greater than 5")
#     else:
#         print("This will not be printed")

#     a) 10 is greater than 5

# 6. What is the output of the following Python code?
#     x = 15
#     if x < 10:
#         print("x is less than 10")
#     elif x < 20:
#         print("x is less than 20 but greater than or equal to 10")
#     else:
#         print("x is 20 or greater")

#     b) x is less than 20 but greater than or equal to 10

# 7. What is the primary purpose of an 'if' statement in Python?
#     a) To execute a specific block of code based on a condition.

# 8. When is an 'else' statement used in conjunction with an 'if' statement?
#     b) To execute the code block if none of the 'if' or 'elif' conditions are True.

# 9. Consider the following Python code. What will be printed if the variable 'num' is greater than or equal to 20?
#     num = 25
#     limit = 20

#     if num >= limit:
#         print("The number is greater than or equal to the limit")
#     else:
#         print("The number is less than the limit")

#     a) The number is greater than or equal to the limit

# 10. Given the Python code snippet:
#     num = 15

#     if num > 10:
#         print("num is greater than 10")

#     What will be the output if this code is executed?

#     a) num is greater than 10

# 11. Given the Python code snippet:
#     x = 15

#     if x > 10 and x < 20:
#         print("x is greater than 10 and less than 20")
#     else:
#         print("x is either less than or equal to 10 or greater than or equal to 20")

#     a) x is greater than 10 and less than 20

# 12. Given the Python code snippet:
#     y = 5

#     if y < 0 or y > 10:
#         print("y is less than 0 or greater than 10")
#     else:
#         print("y is between 0 and 10 (inclusive)")

#     What will be the output if this code is executed?
#     b) y is between 0 and 10 (inclusive)

# 13. Given the Python code snippet:
#     x = 8

#     if x < 10:
#         print("Code block 1: x is less than 10")
#     elif x < 15:
#         print("Code block 2: x is less than 15")
#     elif x < 20:
#         print("Code block 3: x is less than 20")
#     else:
#         print("Code block 4: x is 20 or greater")

#     What will be the output if this code is executed when x is 8?
#     a) Code block 1: x is less than 10

# 14. Given the Python code snippet:
#     y = 25

#     if y < 10:
#         print("Code block 1: y is less than 10")
#     elif y < 15:
#         print("Code block 2: y is less than 15")
#     elif y < 20:
#         print("Code block 3: y is less than 20")
#     else:
#         print("Code block 4: y is 20 or greater")

#     What will be the output if this code is executed when y is 25?
#     d) Code block 4: y is 20 or greater
        
# Quiz. (Dictionaries)
# 1. Which of the following are true of Python dictionaries:
#     a) Dictionaries are mutable
#     c) A dictionary can contain any object type except another dictionary
#     d) Dictionaries can be nested to any depth
#     e) Dictionaries are accessed by key

# 2. Consider this dictionary:
#     d = {'foo': 100, 'bar': 200, 'baz': 300}
#     What is the result of this statement:
#     d['bar':'baz']

#     d) It raises an exception

# 3. Suppose x is defined as follows:
# x = [
#         'a',
#         'b',
#         {
#             'foo': 1,
#             'bar':
#             {
#                 'x': 10,
#                 'y': 20,
#                 'z': 30
#             },
#             'baz': 3
#         },
#         'c',
#         'd'
#     ]
# What is the expression involving x that accesses the value 30?
#----------------------------------- x[2]['bar']['z']



# 4. Select the correct ways to get the value of marks key.
#     student = {
#     "name": "Emma",
#     "class": 9,
#     "marks": 75
#     }

#     b) m = student.get('marks')
#     d) m = student['marks'])

# 5. Dictionary keys must be immutable:
#     a) True

# 6. Select the all correct way to remove the key marks from a dictionary:
#     student = { 
#         "name": "Emma",
#         "class": 9,
#         "marks": 75
#     }

#     a) student.pop("marks")
#     b) del student["marks"]

# 7. What is the output of the following dictionary operation:
#     dict1 = {"name": "Mike", "salary": 8000}
#     temp = dict1.get("age")
#     print(temp)

#     b) None

# 8. Items are accessed by their position in a dictionary and all the keys in a 
# dictionary must be of the same type:
#     b) False

# 9. Select all correct ways to copy a dictionary in Python:
#     a) dict2 = dict1.copy()
#     b) dict2 = dict(dict1)

# 10. Please select all correct ways to empty the following dictionary:
#     student = { 
#         "name": "Emma", 
#         "class": 9, 
#         "marks": 75 
#     }
#     c) student.clear()

# 11. What is the output of the following:
#     sample_dict = dict([
#         ('first', 1),
#         ('second', 2),
#         ('third', 3)
#     ])
#     print(sampleDict)

#     b) Options: SyntaxError: invalid syntax

# 12. Select the correct way to access the value of a history subject:
#     sample_dict = {
#         "class": {
#             "student": {
#                 "name": "Mike",
#                 "marks": {
#                     "physics": 70,
#                     "history": 80
#                 }
#             }
#         }
#     }

#     a) sample_dict['class']['student']['marks']['history']

# 13. Select the correct way to print Emma's age:
#     student = {
#         1: {'name': 'Emma', 'age': '27', 'sex': 'Female'},
#         2: {'name': 'Mike', 'age': '22', 'sex': 'Male'}
#     }

#     b) student[1]["age"]

# 14. What is the output of the following dictionary operation:
#     dict1 = {"name": "Mike", "salary": 8000}
#     temp = dict1.pop("age")
#     print(temp)

#     a) KeyError: 'age'

# 15. What is the output of the following code:
#     dict1 = {"key1": 1, "key2": 2}
#     dict2 = {"key2": 2, "key1": 1}
#     print(dict1 == dict2)

#     a) True

# 16. Select correct ways to create an empty dictionary:
#     a) sample_dict = { }
#     b) sample_dict = dict()
