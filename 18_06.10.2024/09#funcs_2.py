import math

# - Functions -
'''A. Create a function named add_numbers that takes two parameters, a and b, and 
returns their sum. Test the function with values 10 and 15.
'''
def add_numbers(a, b):
    return a + b
result = add_numbers(10, 15)
print(result)


'''B. Create a function named calculate_area that calculates the area of a rectangle. 
Add a docstring explaining what the function does and use type annotations for parameters 
and the return value.
'''
def calculate_area(a: int, b: int):
    return f'Rectangle area: {a} x {b} = {a * b}'
print(calculate_area(10, 5))

'''C. Write a function that takes a string as a parameter and returns the count of vowels (a, e, i, o, u)
in the string.
'''
def vowels_count(value):
    count = 0
    vowels = 'aeiou'
    for x in value:
        if x in vowels:
            count += 1
    return count

print(vowels_count('string'))
    

'''D. Write a function that calculates the factorial of a given number n using a for loop.
'''
def fact(num):
    fact = 1
    while num > 0:
        fact *= num
        num -= 1
    return fact
print(fact(0))

'''E. Write a function that takes a string as a parameter and returns True if the string is a palindrome 
(reads the same forwards and backwards), and False otherwise.
'''
def check_if_palindrome(word: str):
    if word.strip().lower() == word[::-1].strip().lower():
        return True
    else:
        return False
print(check_if_palindrome('Bob'))
print(check_if_palindrome('Alex'))

'''F. Write a function that takes a string as a parameter and returns the reverse of the string. 
Use a for loop to iterate through the characters in the string.
'''
def str_reverse(text: str):
    return text[::-1].lower()
print(str_reverse('school'))

'''G. Write a function that takes a number as a parameter and prints whether it's positive, negative, 
or zero using if-elif-else statements.
'''
def check_if_positive(number: int):
    if number > 0:
        print(f'{number} is positive')
    elif number < 0:
        print(f'{number} is negative')
    else:
        print(f'{number} is zero')
check_if_positive(20)
check_if_positive(-2)
check_if_positive(0)     

'''H. Write a function that takes a list of boolean values as a parameter and returns the count of True
and False values in the list. Use a for loop and if statements.
'''
def booleans_count(value: list):
    booleans = {
        'true': 0,
        'false': 0
    }
    for x in value:
        if x == True:
            booleans['true'] += 1
        elif x == False:
           booleans['false'] += 1
    return booleans
lst = [True, True, False]
print(booleans_count(lst))

'''I. Write a function that checks if a given number is a prime number. Return True if it's prime, and 
False if it's not. Use a for loop and conditionals.
'''
def check_if_prime(number):
    prime = True
    for i in range(2, math.ceil(number**0.5)):
        if number % i == 0:
            prime = False
            break
    return prime
print(check_if_prime(5))   
print(check_if_prime(6)) 

'''J. Write a function that takes a list of numbers as a parameter and returns the largest number in the 
list. Use an if statement to track the largest number.
'''
def find_largest_func(lst: list):
    max = lst[0]
    for x in lst:
        if x > max:
            max = x
    return max
lst = [10, 20, 3, 56, 87, 0, 9]
print(find_largest_func(lst))

'''K. Write a program that calculates the sum of all even numbers from 1 to a given number n. Use a for 
loop and an if statement.
'''
def evens_sum(number):
    total = 0
    for i in range(number):
        if i % 2 == 0:
            total += i
    return total
print(evens_sum(25))

'''L. Write a program that prints numbers from 1 to 10. For multiples of 3, print "Fizz" instead of the 
number, and for multiples of 5, print "Buzz". For numbers that are multiples of both 3 and 5, print "FizzBuzz".
'''
def number_modifying(number):
    if number % 15 == 0:
        return 'FizzBuzz'
    elif number % 5 == 0:
        return 'Buzz'
    elif number % 3 == 0:
        return 'Fizz'
    else:
        return number

for x in range(20):
    print(number_modifying(x))


# Quiz.
# 1. What is a function in Python?
#     b) A block of reusable code

# 2. How do you define a function in Python?
#     a) def function_name()

# 3. What is the purpose of a return statement in a function?
#     c) To return a value from the function

# 4. Can a Python function return multiple values?
#     a) Yes

# 5. What is a docstring in Python?
#     c) A comment used for explaining the purpose and usage of a function, class or module

# 6. How do you write a docstring in a Python function?
#     a) Using triple single-quotes or triple double-quotes at the beginning of the function

# 7. What is the purpose of type annotations in Python?
#     c) To provide hints about the expected types of arguments and return values

# 8. How do you add type annotations to a function in Python?
#     d) By using a colon after the variable name

# 9. What is a type hint in Python?
#     a) A mandatory type requirement for function parameters

# 10. What is the benefit of using type hints in Python?
#     b) It makes the code more readable and self-explanatory

# 11. How do you specify the return type of a function in a type hint?
#     a) By using -> followed by the return type

# 12. What is the purpose of using type annotations for function parameters and return values?
#     c) To make the code more understandable and maintainable

# 13. What does the following Python code snippet do?
#     def greet(name):
#         print(f"Hello, {name}!")

#     greet("Alice")

#     a) Defines a function to greet a person by name

# 14. What is the primary purpose of the following Python function?
#     def calculate_average(numbers):
#         \"\"\"Calculates the average of a list of numbers.\"\"\"
#         total = sum(numbers)
#         count = len(numbers)
#         return total / count

#     c) To calculate the average of a list of numbers

# 15. What is the output of the following Python code snippet?
#     def is_even(num):
#         return num % 2 == 0

#     print(is_even(4))

#     a) True

# 16. How do you call the function is_even from question 15 to check if the number 7 is even?
#     a) is_even(7)

# 17. What does the following Python code snippet do?
#     def print_numbers(n):
#         for i in range(n):
#             print(i)

#     print_numbers(5)

#     a) Prints the numbers 0 to 4

# 18. What does the following Python code snippet do?
#     def absolute_value(num):
#         if num >= 0:
#             return num
#         else:
#             return -num

#     result = absolute_value(-5)

#     b) Calculates the absolute value of a number

# 19. What is the output of the following Python code snippet?
#     def greet(time):
#         if time < 12:
#             return "Good morning!"
#         elif time < 17:
#             return "Good afternoon!"
#         else:
#             return "Good evening!"

#     print(greet(10))

#     a) Good morning!

# 20. What does the following Python code snippet do?
#     def square(num):
#         return num ** 2

#     numbers = [1, 2, 3, 4]
#     squared_numbers = [square(num) for num in numbers]

#     b) Squares each number in the list numbers

# 21. What is the purpose of using functions with loops in Python?
#     b) To modularize code and avoid repetition

# 22. What is the purpose of using functions with if statements in Python?
#     c) To improve the if statement's performance