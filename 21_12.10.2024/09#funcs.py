import logging
import math

logging.basicConfig(
    level=logging.NOTSET, 
    # filename="py_log.log",
    filemode="w",
    format="%(asctime)s %(levelname)s %(message)s"
    )
# - Functions -
'''A. Define a function greet_with_message that takes a username and a 
message (with a default value of "Hello") as parameters and prints 
the message along with the username.
'''
def greet_with_message(username, message='Hello'):
    print(f'{username}, {message}')
greet_with_message('Ali')
greet_with_message('Bob', 'How are you?')

'''B. Write a function calculate_discount that calculates the discounted 
price of an item based on the original price and a discount rate 
(default to 10%). Return the discounted price.
'''
def calculate_discount(price, discount=10):
    result = price - price * discount / 100
    return result
logging.info(f'Default discount: {calculate_discount(50)}')
logging.info(f'30% discount: {calculate_discount(100, 30)}')

'''C. Create a function sum_all that takes any number of arguments using 
the asterisk operator in the parameter definition and returns the sum 
of all the arguments.
'''
def sum_all(*args):
    return sum(*args)
numbers = [3, 5, 17, 23, 89]
sum_numbers = sum_all(numbers)
logging.info(f'Numbers: {numbers}, Sum numbers: {sum_numbers}')

'''D. Write a function calculate_product that takes at least two arguments
and calculates their product. Use the asterisk operator in the parameter 
definition to handle multiple arguments.
'''
def calculate_product(*, shoes, tshirt, **kwargs):
    product_list = [shoes, tshirt, *[x for x in kwargs.values()]]
    print(product_list)
    total = sum(product_list)
    return total
count = calculate_product(shoes=5, tshirt=3, bot=3)
logging.info(count)

'''E. Write a function sum_of_numbers that takes a variable number of integers
as parameters and returns their sum.
'''
def sum_of_numbers(*args):
    return sum(args)
total = (sum_of_numbers(3, 5, 8, 14, 26))
logging.info(f'Result: {total}')

'''F. Create a function calculate_power that takes two parameters: a base number
and an exponent, and returns the result of raising the base to the given exponent.
'''
def calculate_power(base, exponent):
    return base**exponent
logging.info(calculate_power(3, 5))

'''G. Define a function named greet_user that takes a parameter username and prints 
a greeting message like: "Hello, [username]!".
'''
def greet_user(username):
    print(f'Hello, [{username}]!')
    return
greet_user('Bob')

'''H. Write a function called calculate_area that takes the radius of a circle as a 
parameter and returns the area of the circle.
'''
def calculate_area(radius):
    area = math.pi * radius**2
    return area
logging.info(calculate_area(5))

'''I. Create a function average that takes a list of numbers as a parameter and calculates 
the average of those numbers.
'''
def numbers_average(*args: int):
    average = sum(args) / len(args)
    return average
logging.info(numbers_average(3, 15, 56, 37, 89))

'''J. Implement a function maximum_number that takes a variable number of integers as 
parameters and returns the largest number.
'''
def maximum_number(*args: int)->int:
    result = max(args)
    return result
logging.info(maximum_number(3, 57, 90, 27, 1, 83, 8, 9))

'''K. Define a function greet_with_salutation that takes a username and a salutation 
(with a default value of "Mr.") as parameters and prints a greeting using the provided salutation.
'''
def greet_with_salutation(username, salutation='Mr'):
    result = f'Hello, {salutation} {username}'
    return result
logging.info(greet_with_salutation('Bob'))
logging.info(greet_with_salutation('Lucy', 'Ms'))

'''L. Write a function calculate_cost that calculates the total cost of purchasing a
given quantity of items, considering a unit price and tax rate (default tax rate is 5%).
'''
def calculate_cost(price, count, tax=5):
    unit_price = price + price * tax / 100
    total = count * unit_price
    return total
logging.info(calculate_cost(23, 5))
logging.info(calculate_cost(23, 5, 20))

'''M. Create a function concatenate_strings that takes a variable number of strings as parameters 
and concatenates them into a single string, separated by spaces.
'''
def concatenate_strings(*args: str)->str:
    return ' '.join(args)
logging.info(concatenate_strings('one', 'two', 'three'))

'''N. Write a function calculate_sum_and_product that takes at least two numbers as arguments 
and returns both their sum and product. Use the asterisk operator in the parameter definition 
to handle multiple arguments.
'''
def calculate_sum_and_product(arg1, arg2, *args):
    result_sum = arg1 + arg2 + sum(args)
    result_multiple = arg1 * arg2
    for x in args:
        result_multiple *= x
    return {
        'sum': result_sum, 
        'multiple': result_multiple
        }
result = calculate_sum_and_product(4, 15, 98, 56, 72)
result = f'Sum: {result.get('sum')}, Multiple: {result.get('multiple')}'
logging.info(result)

'''O. Write a function find_max_min that takes a list of numbers as a parameter and returns both 
the maximum and minimum numbers from the list. Use if statements to handle edge cases.
'''
def find_max_min(*args):
    try:
        largest = max(args)
        smallest = min(args)
        return {
            'max': largest,
            'min': smallest
        }
    except ValueError as err:
        logging.error(err)
        return 

result = find_max_min()
print(result)
result = find_max_min(3, 46, 74, 82)
logging.info(result)

'''P. Create a function calculate_grade that takes a student's numerical score as a parameter and
returns their corresponding letter grade based on the following scale:
90-100: 'A'
80-89: 'B'
70-79: 'C'
60-69: 'D'
Below 60: 'F'
Handle any invalid scores (less than 0 or greater than 100) by returning 'Invalid Score'.
'''
def decorator_score(func):
    def wrapper(*args, **kwargs):
        letter =  func(*args, **kwargs)
        if letter == None:
            logging.error('Incorrect score')
            return
        return f'Score: {args[0]}, Letter: {letter}'
    return wrapper
@decorator_score
def calculate_grade(score):
    scores = {
        'A': (90, 101),
        'B': (80, 90),
        'C': (70, 80),
        'D': (60, 70),
        'F': (0, 60)
    }
    for key in scores.keys():
        if scores.get(key)[0] <= score < scores.get(key)[1]:
            return key
    return   
print(calculate_grade(-5))
print(calculate_grade(100))

'''Q. Write a function solve_quadratic that takes the coefficients of a quadratic equation 
(a, b, c) as parameters and returns the real roots (if any) of the quadratic equation. 
Use the quadratic formula.
'''
def solve_quadratic(a, b, c):
    D = b**2 - 4 * a * c
    if D < 0:
        logging.error('Not any real roots')
        return
    return {
        'x1': (-b + D**0.5) / (2 * a),
        'x2': (-b - D**0.5) / (2 * a)
    }
logging.info(solve_quadratic(5, 9, 3))
logging.info(solve_quadratic(5, 2, 3))

'''R. Implement a function is_palindrome that takes a string as a parameter and returns True
if the string is a palindrome (reads the same forwards and backwards), and False otherwise.
'''
def is_palindrome(string: str) -> bool:
    string = string.strip().lower()
    length = len(string)
    for i in range(length // 2):
        if string[i] != string[length - 1 - i]:
            return False
    return True
logging.info(is_palindrome('Bobbob'))
logging.info(is_palindrome('Jack'))

'''S. Create a function sort_numbers that takes three numbers as parameters and returns them in 
ascending order as a tuple.
'''
def sort_numbers(num1: int, num2: int, num3: int)->tuple:
    sorted_args = [num1, num2, num3]
    sorted_args.sort()
    return tuple(sorted_args)
logging.info(sort_numbers(1, 2, 1))

'''T. Write a function calculate_tax that takes an income amount and a tax rate as parameters 
and calculates the tax amount. Return a tuple containing the tax amount and the net income 
(income after tax).
'''
def calculate_tax(income_amount: int, tax_rate: int) -> tuple:
    tax = income_amount * tax_rate / 100
    net = income_amount - tax
    return tuple((net, tax))
logging.info(calculate_tax(1000, 18))

'''U. Create a function calculate_discounted_price that takes the original price and a discount 
percentage as parameters. Return a tuple containing the discounted price and the amount saved.
'''
def calculate_discounted_price(price, discont_percentage):
    discount = price * discont_percentage / 100
    discounted_price = price - discount
    return tuple((discounted_price, discount))
logging.info(calculate_discounted_price(300, 25))


'''Quiz.

1. What does the following function do?
    def greet_user(username):
        print("Hello, " + username + "!")

    a) Greets the user with a customized message.

2. Which of the following functions best describes the calculations of the area of a circle?
    a) calculate_circle_area(radius)

3. What is the purpose of a default parameter in a function?
    b) It allows the function to have optional parameters.

4. In Python, how do you pass a variable number of arguments to a function?
    c) Using the asterisk (*) operator in the parameter definition

5. Which of the following functions best describes the calculations of the sum of a list of numbers?
    b) calculate_sum(numbers)
    d) sum_all(*numbers)

6. What does the asterisk (*) operator do in the function definition?
    b) Allows the function to take a variable number of arguments.

7. Consider the following function:
    def greet_user(username="Guest"):
        print("Hello, " + username + "!")

    What is the default value for the username parameter in this function?
    a) "Guest"

8. In the following function, what happens if no value is provided for the message parameter?
    def greet_with_message(username, message="Hello"):
        print(message + ", " + username + "!")

    b) The function uses the default value "Hello" for the message.

9. Which of the following is a valid function definition using default parameters?
    a) def calculate_area(radius, pi=3.14159):

10. Consider the function below:
    def calculate_discount(price, discount_rate=0.1):
        return price * (1 - discount_rate)

    What is the default discount rate used if not provided?
    a) 10%

11. Given the function:
    def multiply(a, b=2):
        return a * b

    If we call multiply(5), what will be the result?
    a) 10

12. In the following function definition, what does the * represent?
    def display_names(*names):
        for name in names:
            print(name)

    b) It allows passing a variable number of names as arguments.

13. Given the function below:
    def greet_with_messages(*messages):
        for message in messages:
            print(message)

    If we call greet_with_messages("Hello", "Bonjour", "Hola"), how many messages will be printed?
    a) 3

14. Consider the function definition:
    def generate_pattern(symbol='*', count=5):
        return symbol * count

    If we call generate_pattern(count=3), what will be the result?
    d) '*****'

15. You have a list of numbers: [12, 5, 78, 43, 67, 89, 45, 23]. What will the function find_max_min return for this list?
    d) (89, 5)

16. If the score provided to the function calculate_grade is 75, what will be the output of the function?
    a) 'C'
   
17. For the quadratic equation with coefficients a=1, b=-5 and
c=6, what will the function solve_quadratic return?
    c) (2, 3)

18. If the input string to the function is_palindrome is "radar", 
what will the function return?
    a) True
      
19. For the input numbers 5, 2, 8, what will be the output of the function sort_numbers?
    a) (2, 5, 8)

20. If the income is $5000 and the tax rate is 20%, what will be the output of 
the function calculate_tax?
    b) (4000, 1000)

21. If the original price is $100 and the discount rate is 25%, what will be the 
output of the function calculate_discounted_price?
    a) (75.0, 25.0)
    '''