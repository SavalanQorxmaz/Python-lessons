from math import pi


# - Functions -
'''A. Define a Python function named greet_user that takes a user's name as a parameter 
and prints a greeting message. Call the function to greet the user by their name.
'''
def greet_user(user: str):
    print(f'Hello {user}')
user = input('User name: ')
greet_user(user)

'''B. Write a function named calculate_area that takes the radius of a circle as a parameter 
and returns the area of the circle. Print the area of a circle with radius 5 using this function.
'''
def calculate_area(radius: int):
    area = pi * radius**2
    print(f'Area is: {area}')

calculate_area(3)
calculate_area(8)

'''C. Create a function named calculate_total_cost that takes the price and quantity of an 
item as parameters and returns the total cost. Print the total cost for an item with a 
price of $10 and a quantity of 3 using this function.
'''
# def str_to_int(value):
#     try:
#         return int(value)
#     except ValueError:
#         print('Incorrect format')
#         return None
    
def calculate_total_cost(price, quantity):
    total = price * quantity
    print(f'price: {price}$\tquantity: {quantity}\tTotal:{total}$')

calculate_total_cost(10,3)

'''D. Write a function named 'hello' that prints "Hello world". Call this function two times.
'''
def hello():
    print('Hello world')

hello()
hello()

'''
Quiz.
1. What is a function in Python?
    a) A named sequence of statements that can be reused.

2. How do you define a function in Python?
    a) Using the def keyword followed by the function name and parameters.

3. What is the purpose of parameters in a Python function?
    b) Parameters specify the input values that the function expects.

4. What is a return statement in a Python function?
    a) It exits the function and returns a value to the calling code.
    
5. How can you call a function in Python?
    c) Using the function name followed by parentheses and providing the required arguments.

6. What is the difference between parameters and arguments in a Python function?
    c) Parameters are the values specified in the function definition, and arguments 
    are the values passed to a function when calling it.

7. Write a Python function named add_numbers that takes two parameters a and b and returns their sum.
    c)
    def add_numbers(a, b):
        return a + b

8. Write a Python function named is_even that takes a single parameter num and returns True if the number
is even and False otherwise.
    a)
    def is_even(num):
        return num % 2 == 0

9. Write a Python function named greet that takes a single parameter name and prints a greeting message.
    a)
    def greet(name):
        print("Hello, " + name + "!")

10. Write a Python function named calculate_average that takes a list of numbers and returns their average.
    a)
    def calculate_average(numbers):
        return sum(numbers) / len(numbers)

11. Write a Python function named calculate_power that takes two parameters base and exponent 
and returns the result of base raised to the power of exponent.
    a)
    def calculate_power(base, exponent):
        return base**exponent

12. Consider the following Python program:
    def print_greeting():
        print("Hello, world!")

    print_greeting()

    What will this program print?
    a) Hello, world!

13. Consider the following Python program:
    def print_numbers():
        print(1)
        print(2)
        print(3)

    print_numbers()

    What will this program print?
    a)
    1
    2
    3
    
14. Consider the following Python program:
    def print_multiple_messages():
        print("Hello!")
        print("How are you?")
        print("Goodbye!")

    print_multiple_messages()

    What will this program print?
    a)
    Hello!
    How are you?
    Goodbye!

15. Consider the following Python program:
    def print_values():
        print("Value 1")
        print("Value 2")
        print("Value 3")

    print_values()

    What will this program print?
    a)
    Value 1
    Value 2
    Value 3

16. Consider the following Python program:
    def print_repeated_message():
    for _ in range(3):
        print("This is a repeated message.")

    print_repeated_message()

    What will this program print?
    a)
    This is a repeated message.
    This is a repeated message.
    This is a repeated message.

17. What is the purpose of the return keyword in a Python function?
    b) To return a value or object from the function to the caller.

18. What happens if a function in Python does not contain a return statement?
    d) The function will exit without returning anything.

19. What does the return statement without a value return in Python?
    c) It returns None.

20. What is the data type of the value that can be returned by a Python function?
    c) The data type is determined by the return statement.

21. Consider the following function:
    def greet():
        print("Hello, world!")

    result = greet()

    What will be the value of result after calling greet()?
    a) None

22. Can a Python function have both a return statement and print statements inside it?
    a) Yes
'''