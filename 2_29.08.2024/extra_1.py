import math

# 1. Write a program that takes a string as input and prints the reversed string.
# 2. Write a program that formats a string using variables for name, age, and city.
# 3. Write a program that takes the radius of a circle as input and calculates the area.
# 4. Write a program that takes a string as input and converts it to uppercase.
# 5. Write a program that takes three integers as input and prints the maximum.

# 1
text = 'Mercedes'
reverce_1 = text[::-1]
print(f'{reverce_1=}')

length = len(text) 
reverce_2 = ''
for i in range(length):
   reverce_2 +=  text[length - i - 1]
print(f'{reverce_2=}')

# 2
name = 'Ali'
age = 20
city = 'Baku'
method_1 = f'\n Name: {name}\n Age: {age}\n City: {city}'
print(f'Method 1:{method_1}')

method_2 = '\n Name: {}\n Age: {}\n City: {}'.format(name, age, city)
print('Method 2:{}'.format(method_2))

method_3 = '\n Name: %s\n Age: %s\n City: %s' % (name, age, city)
print('Method 3:%s'% method_3)

# 3
radius = input('Circle radius: ')
def check_if_input_is_float(value):
    try:
        if float(value):
            return True
    except ValueError:
        return False
    
while not check_if_input_is_float(radius):
    print('Type number:')
    radius = input('Circle radius: ')

radius = float(radius)
pi = math.pi
area = pi * radius**2
print(area)
    
# 4
text = input('Insert text: ')
upper_text = text.upper()
print('Upper Text: '+ upper_text)

# 5
print('Find maximum')
my_list = []
def convert_to_integer(value):
    try:
        if float(value):
            return round(float(value))
    except ValueError:
        return False

for i in range(3):
    value = input(f'number {i + 1}: ')
    while  convert_to_integer(value) == False:
        print('It is not number')
        value = input(f'number {i + 1}: ')
    if convert_to_integer(value) is None:
        my_list.append(0)
    else: my_list.append(convert_to_integer(value))

print(f'List: {my_list}')
my_list.sort()
print(f'Maximum: {my_list[2]}')

    

