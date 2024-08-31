import math
# Integers

speed = 70
limit = 100
difference = limit - speed
print(difference)

amount = 10
double_amount = amount * 2
triple_amount = amount * 3
print(f'{amount=}')
print('double amount =', double_amount)
print('Triple amount = %s' % triple_amount)

distance = 1000
passed_distance = 200
print('Difference = {}'.format(distance - passed_distance))

number_one = 99
number_two = 58
number_three = number_one + number_two
print(number_three)

a = 15
b = 35
c = 20
result = a + b - c
print(c)

my_number = 4
print(pow(my_number, 3))

# Floats

temperature = 30.8
weight = 5.84
length = 3.72
space = 347.652
print(f'{temperature=}\n{weight=}\n{length}\n{space=}')

x = 1.23
double_x = x * 2
print('x= {}\ny= {}'.format(x, double_x))


my_x = 36.652
my_y = 75.893
square_root = pow(my_x, 0.5)
sub_module = abs(my_x - my_y)
round_x = round(my_x)
round_y = round(my_y, 2)
print(f'''
x= {my_x}
y= {my_y}
sqroot= {square_root}
submodule= {sub_module}
round x(0)= {round_x}
round y(2)= {round_y}
''')

#  Built-in functions

long_sentence = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
print(len(long_sentence))

accurate_number = 10.35762
print(accurate_number)

rounded_accurate_number = round(accurate_number, 2)
print(rounded_accurate_number)

rounded_accurate_number = round(accurate_number, 3)
print(rounded_accurate_number)

rounded_integer = round(175233, -3)
print(rounded_integer)

# Math module
'''

pow(a, 2) 
pow(x, y) 
math.ceil(x)
math.floor(x)
pi = round(3.141418, 2)

C. 
s = 700
a = math.sqrt(s)

D.
b = a + 5
p = (a + b) * 2 = 100
a + b = 50
a + a + 5 = 50
2 * a = 45
a = 22.5
b = 22.5 + 5 = 27.5
s = 22.5 * 27.5

math.floor(5.7) ---> 5
math.floor(5.7) ---> 6

'''

# Expression

result = ((5 * 5 + 5 // (5 + math.fmod(5, 5)) // 5) + 5**5 + 5 - 5**0)
print("Result A=", result)

result = (20 + 30 * (15 - 7) // (3 + 4 % 2) + 10**2 // 5) + 2**6 + 50 - 3**1
print("Result B=", result)

result = (70 - 25 + 3 * (8 + 4) // (6 + 9 % 3) + 15**2 // 7) + 4**3 + 90 - 2**4
print("Result C=", result)

# Chat GPT's Homework

a = 6
p = 6 * 4

current = 150 - 47.25 + 30.50
result = 150 - current
print(result)

speed = 80
result = speed * 1.5 
print(result)

# ------------

print(f'''
{round(4.25 + 2.68, 2)}
{round(9.75 - 3.85, 2)}
{round(3.5 * 1.2, 2)}
{round(7.8 / 2.5, 2)}
''')

pi = math.pi
r = 7
circumference  = 2 * pi * r
print(f'{circumference=}')

print(math.sqrt(16))
print(math.sqrt(25))
print(round(math.sqrt(10),2))

print(math.pow(2, 5)) # 32
print(math.pow(3, 4))   # 81

print(math.ceil(6.1))  # 7
print(math.ceil(10.9))  # 11
print(math.ceil(-2.3))  # -2

print(math.floor(4.7))  # 4
print(math.floor(9.2))  # 9
print(math.floor(-3.8))  # -4

# Quiz

'''

1. Which of the following is a comparison operator in Python?
    c) ==

2. What is the result of 15.5 - 7.2 rounded to two decimal places?
    a) 8.3

3. What is the result of 1.5 - 1.0 rounded to two decimal places?
    a) .5

4. If 'a = 12' and 'b = 7', which expressions are True?
    b) a > b

5. What is the value of 20/4?
    d) 5.0

6. Which of the following are integers?
    b) -15

7. What is the absolute value of -25?
    a) 25

8. If 'x = 5' and 'y = 8', what is the value of x^y (x raised to power of y)?
    d) 390625

9. What does the math module in Python provide?
    c) Advanced geometry calculations.

10. Given the equation 3 x 8 - 5, what is the correct result?
    a) 19

11. What is the result of 17 + 23?
    b) 40

12. What is the result of "17" + "23"?
    d) "1723"

'''
