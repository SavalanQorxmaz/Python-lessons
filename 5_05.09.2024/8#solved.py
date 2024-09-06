import string
import getpass
import time
import math
import random


# - Programs -
# A
name = input('Input your name: ')

age = input('Input your age')
def check_input_is_int(value): # Function check age type
    try:
        if int(value):
            return True
    except ValueError:
        return False
    
while not check_input_is_int(age): # If age is not number type, need to type again
    age = input('Input your age with number: ')

nationality = input('Nationality: ')

print(f'Name: {name}\nAge: {age}\nNationality: {nationality}')

# B
numbers = []
def check_input_is_number(value): 
    try:
        if float(value):
            return True
    except ValueError:
        return False
for i in range(2):
    number = input(f'Number {i + 1}: ')
    while not check_input_is_number(number):
        number = input(f'Please type number {i + 1} correct: ')
    numbers.append(float(number))    
sum = numbers[0] + numbers[1]
print(f'Sum: {int(sum)}')

# C
first_text = input('First variable: ')
second_text = input('Second variable: ')
concat_text = first_text + second_text
print(f'New text: {concat_text}')

# - Modules -

# String module
all_ascii = string.ascii_letters
new_word = input('Type word: ')
is_new_word_ascii = True
for x in new_word:
    if x not in all_ascii:
        is_new_word_ascii = is_new_word_ascii and False
if is_new_word_ascii:
    print('Your word ascii')
else: 
    print('Your word is not ascii')

# ascii_uppercase, asii.lowercase
all_uppercase = string.ascii_uppercase
all_lowercase = string.ascii_lowercase
new_word = input('Type Password: ')
has_lowercase = False
has_uppercase = False
for x in new_word:
    if x in all_lowercase:
        has_lowercase = has_lowercase or True
    if x in all_uppercase:
        has_uppercase = has_uppercase or True
if has_lowercase and has_uppercase:
    print('Your password correct')
else: 
    print('Your password incorrect')


# getpass module
password = getpass.getpass(prompt = 'Enter the password(123)') 
if password == '123': 
    print('Correct') 
else: 
    print('Incorrect') 

# - Python Tricks -

a = "Hello"
b = 5
print(f'Before: {a=} {b=}')
a, b = b, a
print(f'After: {a=} {b=}')


pi = 3.1415
gravity = 9.8
oil = 82.12
date = time.ctime()

# - Math -
# A
value = 57_999.99
rounded_value = round(value)
print(f'Rounded value = {rounded_value}')

# B
sqrt_value = math.sqrt(value)
rounded_sqrt_value = round(sqrt_value, 1)
print(rounded_sqrt_value)

# C
value = 0.0592481
nearest_int_value = round(value)
print(f'rounded value: {nearest_int_value}')

value = 5.5
value_power5 = value**5
print(value_power5)


# - NoneType -

print(type(None))
print(bool(None))

value = None
if value is None:
    print('value is None')


# - Built-ins -

def power_function(value, power):
    return value**power
x = 5
y = 3
power1 = power_function(y, x)
power2 = (power_function(x, y))
print(f'{power1=}\n{power2=}')

x = input('Insert Integer Number: ')
y = input('Insert Another Integer Number: ')
result = int(x)**int(y)
print(f'result: {result}')

# - String Formattings -

pi = math.pi
rounded_pi = f'{pi:.2f}'
print(pi)
print(rounded_pi)

big_int = 5_000_000
print(f'Current big_int: {big_int}')
big_int_new_decoration = f'big_int new decoration: {big_int:,}'
print(big_int_new_decoration)

initial_apple_count = 28
eaten_apple = 4
left_apple_percentage =  (28 - 4) * 100 / 28
print(f'Left apple Percentage: {left_apple_percentage:.0f}')

# - Chat GPT's Homework -

fruits = ['apple', 'banana','kiwi']
fruit = random.choice(fruits)
print(fruit)

number = random.randrange(0,1001) / 1000
print(number)

brands = ['BMW', 'Mercedes', 'Audi', 'GMC', 'Nissan', 'Hyundai', 'Mercedes', 'GMC']
brand = random.choice(brands)
print(brand)

random_given_range = random.randrange(-1000, 1000)
print(random_given_range)

random.shuffle(brands)
print(brands)

# 2
randint_5_10 = random.randint(5, 10)
print(randint_5_10)

# 3
random_0_1 = random.random()
print(random_0_1)

# 4
random_sample = random.sample(brands, 3)
print(random_sample)

brands_set = list(set(brands))
random_sample_set = random.sample(brands_set, 3)
print(random_sample_set)

new_list = brands[:4]
print(new_list)

# 5
value = 25
sq_rt = math.sqrt(value)
print(f'{sq_rt= }')

# 6
pi = math.pi
print(f'{pi= }')

# 7
x = 7.6
x_ceil = math.ceil(x)
print(f'{x_ceil= }')

# 8
for i in range(5):
    print(random.randint(50, 100), end=', ')
print()

# 9
float_value = input('Insert float type number: ')
def check_input_is_float(value): 
    try:
        if int(value):
            return True
    except ValueError:
        return False
while not check_input_is_float(float_value):
    float_value = input('Insert float type number: ')
sqrt_value = math.sqrt(float(float_value))
print(f'{value= }, {sqrt_value= }')

# 10
rolling_dice = random.randint(1,6)
print(f'{rolling_dice= }')

# - Interview Questions -
'''
1. What does the None keyword represent in Python?
    a) A special value that represents an empty string

2. Which type is assigned to a variable that has no value assigned to it in Python?
    b) NoneType

3. What is the result of evaluating the expression: type(None)?
    a) <class 'NoneType'>

4. Which statement assigns the value None to the variable 'result'?
    b) result = None

5. What is the correct way to check if a variable value is set to None?
    d) if value is None:

6. Can None be used in arithmetic operations in Python?
    b) No, trying to perform arithmetic with None will result in an error.

7. What does the math.floor(x) function do?
    b) Returns the largest integer less than or equal to x.

8. Which of the following is the correct way to import the 'math' module in Python?
    b) import math

9. The math.ceil(x) function does what?
    b) Returns the value of x rounded up to the nearest integer.

10. What does the math.pow(x, y) function do?
    c) Calculates the power of x raised to the yth power.

11. The math.sqrt(x) function is used to:
    a) Calculate the square root of x.

12. What is the output of the following code:
    import math
    value = 3.05
    print(math.floor(value))

    a) 3

13. What is the output of the following code:
    from math import pi
    a = round(pi, 2)
    print(a * 2)

    c) 6.28

14. What is the purpose of the random.choice(seq) function?
    b) It selects a random element from the sequence seq.

15. Which of the following methods is used to select multiple unique random 
elements from a sequence?
    b) random.sample(seq, count)

16. How would you import the random module correctly in Python?
    d) import random

17. If you want to generate a random integer between 1 and 100 (inclusive), 
which random module method would you use?
    a) random.randint(1, 100)

18. In Python, what is the process of combining multiple strings into one?
    a) Concatenation

19. What does the ascii_letters constant include?
    c) Both uppercase and lowercase letters

20. Which PEP provides recommendations and guidelines for writing clean, readable, and maintainable Python code?
    b) PEP 8

21. What is the primary purpose of the "as" keyword in Python's "import" statement?
    a) It renames the module being imported.
'''