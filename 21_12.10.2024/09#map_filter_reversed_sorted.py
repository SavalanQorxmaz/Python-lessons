import logging
import math
import time
import datetime
import re
import lorem_text
import lorem_text.lorem
import random
import h09_funcs
logging.basicConfig(
    level=logging.NOTSET, 
    # filename="py_log.log",
    filemode="w",
    format="%(asctime)s %(levelname)s %(message)s"
    )
info = logging.info

# - Map -
'''A. Create a function that takes a list of numbers and uses the map() function to 
double each number in the list.
'''
numbers = [2, 7, 34, 67, 54, 21]
double_numbers = list(map(lambda x: x * 2, numbers))
info(double_numbers)

'''B. Write a function that takes a list of temperatures in Celsius and uses map() 
to convert them to Fahrenheit using the appropriate conversion formula.
'''
temperatures = [30, 40, -2, -80, 22]
def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32
fahreheit_list = tuple(map(celsius_to_fahrenheit, temperatures))
info(fahreheit_list)

'''C. Implement a function that takes a list of numbers and uses the map() function to 
'''

def mapping(*, func, lst: list) ->map:
    return map(func, lst)
custom_func = lambda x: x + 5
info(list(mapping(func = custom_func , lst = [1, 2, 3])))

'''D. Write a function that takes a list of names and uses map() to format them as "Hello, {name}!".
'''
def greeting(name):
    return f'Hello, {name}!'
names = ['Ali', 'Hasan', 'Ahmad']
greeting_list = list(map(greeting, names))
info(greeting_list)

'''E. Create a function that takes a list of numbers and uses the map() function to generate a 
power series for each number, up to a specified exponent.
'''
def power_f(power):
    return lambda x: x**power
numbers = [2, 3, 5, 8]
power_5 = power_f(5)
power_2 = power_f(2)
lst_power5 = list(map(power_5, numbers))
lst_power2 = list(map(power_2, numbers))
info(lst_power2)
info(lst_power5)

'''F. Write a function that takes two lists of strings and uses map() to concatenate the elements 
of the same index from both lists.
'''
def concatenate_if_index_same(lst1, lst2):
    concat  = lambda x, y: str(x) + str(y)
    result = list(map(concat, lst1, lst2))
    return result

lst1 = [1, 2, 3, 4, 5]
lst2 = [5, 6, 7, 8, 9, 13]
info(concatenate_if_index_same(lst1, lst2))

'''G. Create a function that takes a list of floats and uses the map() function to round each float 
to a specified number of decimal places.
'''
def round_f(decimal):
    return lambda x: round(x, decimal)
round2 = round_f(2)
round0 = round_f(0)
floats = [2.345, 3, 4.9, 6.678]
floats_round2 = list(map(round2, floats))
floats_round0 = list(map(round0, floats))
info(floats_round2)
info(floats_round0)

'''H. Write a function that takes a list of prices and uses map() to apply a discount percentage to each price.
'''
prices = [25, 70, 90, 34, 62, 80]
def discount_f(lst: list, discount: int) -> map:
    return map(lambda x: x * (100-discount) / 100, lst)
discounted_price = list(discount_f(prices, 20))
info(discounted_price)


'''I. Implement a function that takes a list of sentences and uses map() to encrypt each sentence using 
a simple encryption algorithm.
'''
def encrypt_algoritm(sentence):
    result = ''
    for char in sentence:
        new_ord = ord(char) + 11
        length = len(str(new_ord))
        rest = 4 - length
        result += f'{'0'*rest}{str(new_ord)}'
    return result
sentences = ['salam, necesen', 'tesekkur', 'hellow world']
encrypted_sentences = list(map(encrypt_algoritm, sentences))
info(encrypted_sentences)


'''J. Create a function that takes a list of words and uses map() to count the number of vowels in each word.
'''
def calculate_vowels_count(text):
    count = 0
    vowels = 'aioue'
    length = len(text)
    while length > 0:
        if text[length-1] in vowels:
            count +=1
        length -=1
    return count
words = ['hello', 'text', 'sentence', 'vowels', 'list-tuple']
vowels_list = list(map(calculate_vowels_count, words))
info(vowels_list)

'''K. Write a function that takes a list of strings and uses map() to return a list of lengths for each string.
'''
def calculate_text_length(text:str) -> int:
    return len(text)
words = ['hello', 'text', 'sentence', 'vowels', 'list-tuple']
words_length_list = list(map(calculate_text_length, words))
info (words_length_list)

# - Filter -
'''A. Create a function that takes a list of numbers and uses the filter() function to 
return a new list containing only the even numbers.
'''
numbers = [1, 34, 56, 7, 89, 98, 43, 0, 23, 45]
even_numbers = tuple(filter(lambda x: x % 2 == 0, numbers))
info(even_numbers)

'''B. Write a function that takes a list of numbers and uses the filter() function to 
return a new list containing only the prime numbers.
'''
def check_if_number_prime(number):
    length = round(number**0.5)
    for i in range(2, length + 1):
        if number % i == 0:
            return False
    else:
        return True
numbers = [1, 34, 56, 7, 89, 98, 43, 0, 23, 45]
prime_numbers = list(filter(check_if_number_prime, numbers))
info(prime_numbers)

'''C. Implement a function that filters a list of strings to return a new tuple containing 
only the words that are palindromes.
'''
def check_if_palindrome(text:str) -> bool:
    text = text.strip().lower()
    length = len(text)
    for i in range(length // 2):
        if text[i] != text[-i - 1]:
            return False
    return True
words = ['hello', 'bob', 'world', 'radar']
palindromes = tuple(filter(check_if_palindrome, words))
info(palindromes)            

'''D. Given a list of dictionaries representing employees and their salaries, use filter() 
to create a new list of employees whose salary is above a specified threshold.
'''
employees = {
    'bob': 3000,
    'jack': 1200,
    'lucy': 1600,
    'jenifer': 2800
}
def check_high_salary(employee) -> bool:
    if  employee[1] > 2000:
        return True
    return False
high_salary_employee = dict(filter(check_high_salary, employees.items()))
info(high_salary_employee)

'''E. Write a function that takes a list of file names and filters it to return a new list 
containing only files with a specified file extension.
'''
def check_file_extension(name: str) -> bool:
    name_list = name.split('.')
    if name_list[-1] == 'txt':
        return True
    return False
file_list = ['test.txt', 'run.exe', 'list.txt', 'spool.bat']
txt_files = list(filter(check_file_extension, file_list))
info(txt_files)

'''F. Create a function that takes a dictionary of student names and their corresponding grades, 
and uses filter() to return a new dictionary containing only students who passed (grades above 
a certain threshold).
'''
students = {
    'Ali': 75,
    'Hasan': 38,
    'Lale': 52,
    'Nigar': 90,
    'Leman':21
}
def check_if_student_passed(student):
    if student[1] > 50:
        return True
    return False
passed_student = dict(filter(check_if_student_passed, students.items()))
info(passed_student)

'''G. Implement a function that takes a mixed list of data types (integers, strings, floats) and 
filters it to return separate lists for each data type.
'''
def check_data_type(dt):
    return lambda x: dt == type(x)
mix = [1, 'a', True, (1, 2), 34, False]
check_bool = check_data_type(bool)
check_int = check_data_type(int)
info(list(filter(check_bool, mix)))
info(list(filter(check_int, mix)))

'''H. Prompt the user to enter a condition, then use the filter() function to filter a given list 
of numbers based on the user-provided condition.
'''

try:
    user_input = input('enter condition (>100, < 50, =25 etc.): ')
    condition = None
    for x in user_input:
        if x in '<>=':
            condition = x
            break
    else:
        logging.error('Not any condition')
    digits ='0123456789'
    index = -1
    number = None
    for i, x in enumerate(user_input):
        if x in digits:
            index = i
            number = x
            for j in range(index + 1, len(user_input)):
                if user_input[j] in digits:
                    number += user_input[j]
                else:
                    break
            break
    else:
        logging.error('Not any digit')
             
except TypeError as err:
    logging.error(err)

def check_user_condition(condition, limit):
    try:
        limit = int(limit)
        if condition == '=':
            return lambda x: x == limit
        elif condition == '<':
            return lambda x: x < limit
        elif condition == '>':
            return lambda x: x > limit
        else:
            return lambda x: True
    except TypeError:
        logging.error('no number')
        return lambda x: True
user_condition = check_user_condition(condition, number)

numbers = [1, 23, 45, 89, 100, 23, 45, 900, 678, 5, 43, 56, 456]

user_list = list(filter(user_condition, numbers))
info(user_list)

'''I. Write a function that takes a list of strings and filters it to return a new list containing 
only strings that contain a specific substring.
'''
strings = ['hello', 'below', 'world', 'low']
def check_if_has_substring(substring: str) -> bool:
    return lambda x: substring in x
sub_lo = check_if_has_substring('lo')
sublist = list(filter(sub_lo, strings))
info(sublist)

'''J. Implement a function that takes a list of strings and filters it to return a new list containing 
strings with a specified character appearing a certain number of times.
'''
strings = ['hello', 'below', 'world', 'low', 'killer']
def check_if_has_char(char: str) -> bool:
    return lambda x: x.count(char) > 1
sub_lo = check_if_has_char('l')
sublist = list(filter(sub_lo, strings))
info(sublist)

'''K. Create a function that takes a list of integers and uses the filter() function to return a 
new list containing only those numbers for which a specified mathematical function (e.g., square, 
cube) yields a prime result.
'''
numbers = range(0, 100)
def check_math_func(func):
    return lambda x: func(x)
def square_f(number):
    return round(number**0.5) == number**0.5
def cube_f(number):
    return round(number**(1/3)) == number**(1/3)

cube_func = check_math_func(cube_f)
square_func = check_math_func(square_f)
cube_list = list(filter(cube_func, numbers))
square_list = list(filter(square_func, numbers))
info(cube_list)
info(square_list)

'''L. Write a function that takes a list of date objects and filters it to return a new list containing 
dates within a specified range.
'''
startdate = datetime.datetime(2023, 1, 1)
enddate = datetime.datetime(2024, 5, 31)

date_list = [(2021, 10, 2), (2024, 10, 1), (2025, 1, 1), (2023, 12, 12), (2023, 12, 31)]

def date_range_f(startdate, enddate):
    return lambda x: datetime.datetime(*startdate) < datetime.datetime(*x) < datetime.datetime(*enddate)
custom_range = date_range_f((2023, 1, 1), (2024, 1, 1))
# print(datetime.datetime(year=2024, month=10, day=1) > datetime.datetime(year=2023, month=10, day=1))
date_range_list = list(filter(custom_range, date_list))
info(date_range_list)


'''M. Given a list of cities and their corresponding countries, use filter() to return a new list 
containing cities from a specific country.
'''
cities = ['baku:azerbaijan', 'ankara:turkiye', 'ganja:azerbaijan', 'new-york:usa', 'istanbul:turkiye', 'london:britain', 'adana:turkiye']

def find_country(country: str):
    return lambda x: x.split(':')[1] == country
find_turkiye = find_country('turkiye')
turkiyes_cities = list(filter(find_turkiye, cities))
info(turkiyes_cities)

'''N. Create a function that takes a list of product objects and uses the filter() function to return a 
new list containing only available products.
'''
products = ['sugar', 'tea', 'apple', 'banana', 'pear', 'onion']

sugar = list(filter(lambda x: x== 'sugar', products))
info(sugar)


'''O. Implement a function that takes a list and uses filter() to return a new list containing only 
the unique elements.
'''
lst = ['banana', 'apple', 'onion', 'apple', 'pear', 'kiwi', 'banana']
unions_list = list(filter(lambda x: lst.count(x) < 2, lst))
info(unions_list)

'''P. Write a function that takes a list of words and filters it to return a new list containing only 
anagrams of a specified word.
'''
anagrams = ['post', 'qara', 'kitab']
words = ['post', 'kitab', 'meyve', 'ayri']
def find_anagram(word:str) -> bool:
    try:
        return anagrams.index(word) > -1
    except ValueError:
        return False
anagram_list = list(filter(find_anagram, words))
info(anagram_list)
        
        

'''Q. Given a list of numeric data, use filter() to return a new list containing elements within a 
specified range.
'''
def check_if_number_in_range(start: int, end: int)-> bool:
    return lambda x: start < x < end
numbers = [1, 24, 45, 67, 78, 98, 43, 123, 6, 94, 2]

range_20_50 = check_if_number_in_range(19, 51)
new_list = list(filter(range_20_50, numbers))
info(new_list)

'''R. Create a function that takes a list of strings and uses filter() to return a new list containing 
only strings that match a specific regular expression.
'''
lst = ['banana', 'apple', 'onion', 'berry', 'pear', 'kiwi', 'sugar']
def regex_f(subword):
    return lambda x: len(re.findall(subword, x)) > 0
exp = regex_f('ar')

new_list = list(filter(exp, lst))
info(new_list)

# - Reversed -
'''A. Write a function that takes a list of elements and uses the reversed() function to reverse the 
order of elements in the list.
'''
lst = [1, 2, 3, 4]
info(list(reversed(lst)))

'''B. Create a function that takes a string and uses reversed() to reverse the characters in the string.
'''
text = 'hello world'
reversed_text = ''.join(list(reversed(text)))
info(reversed_text)

'''C. Implement a function that takes a tuple and uses reversed() to reverse the order of elements in the tuple.
'''
my_tuple = (('hello', 'world', 'book', 'pen', 'sentence', 'water'))
reversed_tuple = tuple(reversed(my_tuple))
info(reversed_tuple)

'''D. Write a function that takes a sentence and uses reversed() to reverse the order of words in the sentence.
'''
sentence = lorem_text.lorem.sentence()
reversed_sentence = reversed(sentence.split())
info(' '.join(reversed_sentence))

'''E. Create a function that takes a dictionary and uses reversed() to reverse the order of keys and values.
'''
my_dict = {
    'writer': 'Dostoyevski',
    'fruit': 'apple',
    'vegetable': 'onion',
    'number': 2
}
reversed_dict = []
for x in my_dict.items():
    reversed_dict.append(tuple(reversed(x)))
    print(x)
reversed_dict = dict(reversed_dict)
print(reversed_dict)

'''F. Implement a function that takes a linked list and uses reversed() to reverse the order of nodes in the linked list.
'''
order = {
    1: [2, 4, None],
    2: [3, None],
    3: [1, 5, None],
    4: [5, None],
    5: [2, None]
}
reversed_order = dict(zip(list(reversed(order)), order.values()))
info(reversed_order)

'''G. Write a function that takes a queue and uses reversed() to reverse the order of elements in the queue.
'''
numbers = [1, 25, 45, 67, 78, 98, 43, 123, 6, 94, 2]
selected = random.choice(numbers)
index = numbers.index(selected)
info(index)
reversed_list = [x for i,x in enumerate(numbers) if i < index] + list(reversed([x for i, x in enumerate(numbers) if i >= index]))
info(reversed_list)
    

'''H. Create a function that takes a stack and uses reversed() to reverse the order of elements in the stack.
'''
stack = [1, 25, 45, 67, 78, 98, 43, 123, 6, 94, 2]
reversed_stack = list(reversed(stack))
info(reversed_stack)

'''I. Implement a function that takes a list of elements and uses reversed() to reverse the elements at odd 
indices, while keeping the elements at even indices unchanged.
'''
numbers = [x for x in range(1, 11)]
odd_reversed_tuple = list(zip(list(reversed([x for x in numbers if x % 2 != 0])), [x for x in numbers if x % 2 == 0] ))
odd_reversed = []
for x in odd_reversed_tuple:
    odd_reversed.extend(list(x))
info(odd_reversed)

'''J. Write a function that takes a binary number as a string and uses reversed() to reverse the binary digits.
'''
def reverse_binary(binary: str):
    binary_split = [x for x in binary]
    result = reversed(binary_split)
    return ''.join(list(result))
info(reverse_binary('11010'))

'''K. Create a function that takes a 2D matrix and uses reversed() to reverse the rows of the matrix.
'''
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def reverse_matrix(matrix:list[list]):
    for i, x in enumerate(matrix):
        matrix[i] = list(reversed(x))
    return matrix
info(reverse_matrix(matrix))
    

'''L. Implement a function that takes a string and uses reversed() to reverse the characters in each substring 
separated by a specific delimiter.
'''
string = 'Veritatis tenetur facere nesciunt dolor, voluptatem consequuntur blanditiis dignissimos dolore error'
substring = 'dolor'
def reverse_substring(sentence: str, word: str):
    reversed_word = ''.join(reversed(word))
    reversed_string = re.sub(word, reversed_word, string)
    return reversed_string
info(reverse_substring(string, substring))

# - Sorted -
'''A. Write a function that takes a list of numbers and uses the sorted() function to return a new list with 
the numbers sorted in ascending order.
'''
numbers = [1, 25, 45, 67, 78, 98, 43, 123, 6, 94, 2]
sorted_numbers = sorted(numbers, reverse=False)
info(sorted_numbers)

'''B. Create a function that takes a list of numbers and uses the sorted() function to return a new list with 
the numbers sorted in descending order.
'''
def f_sort_descending(lst: list) -> list:
    return sorted(lst, reverse=True)
numbers = [1, 25, 45, 67, 78, 98, 43, 123, 6, 94, 2]
info(f_sort_descending(numbers))

'''C. Implement a function that takes a list of strings and uses the sorted() function to return a new list 
with the strings sorted by their lengths.
'''
def f_sort_by_length(strings: list) -> list:
    def f_key(word):
        return len(word)
    return sorted(strings, key=f_key)
strings = 'Implement a function that takes a list of strings and uses the'.split()
info(f_sort_by_length(strings))

'''D. Write a function that takes a list of tuples and uses the sorted() function to return a new list with 
the tuples sorted based on their second element.
'''
def f_sort_tuple_second_element(lst:list) -> list:
    def f_tuple_second_element(tup: tuple)-> tuple:
        return tup[1]
    return sorted(lst, key=f_tuple_second_element)
tuples = [(1, 9), (2, 8), (3, 7), (4, 6)]
info(f_sort_tuple_second_element(tuples))


'''E. Create a function that takes a dictionary and uses the sorted() function to return a new dictionary 
with its items sorted by their values.
'''

def f_sort_by_value(dictionary: dict) -> dict:
    return lambda x: dictionary.get(x)
my_dict = {
    'a':134,
    'b': 243,
    'c': 37,
    'd': 49
}
get_value = f_sort_by_value(my_dict)

sorted_keys = sorted(my_dict, key=get_value)
sorted_dict = {}
for x in sorted_keys:
    sorted_dict.update({x: my_dict.get(x)})
info(sorted_dict)

'''F. Implement a function that takes a list of strings and uses the sorted() function to return a new list 
with the strings sorted in a case-insensitive manner.
'''
def f_sort_by_word(lst: list)-> list:
    ins_word = lambda x: x.lower()
    return sorted(lst, key=ins_word)
sentence = 'Implement a function that takes a List of strings and Uses'
strings = sentence.split()
info(f_sort_by_word(strings))


'''G. Write a function that takes a list of custom objects and uses the sorted() function to return a new list 
with the objects sorted based on a specified attribute.
'''
objects = [
    {
        'name': 'Fatma',
        'surname': 'Aliyeva',
        'age': 40
    },
     {
        'name': 'Fatima',
        'surname': 'Valiyeva',
        'age': 25
    },
      {
        'name': 'Leman',
        'surname': 'Agayeva',
        'age': 18
    },
       {
        'name': 'Sabina',
        'surname': 'Hasanova',
        'age': 30
    }
]

def f_sort_data_by_age(obj:dict)-> dict:
    return_age = lambda x: x.get('age')
    sorted_dict = sorted(obj, key=return_age)
        
    return sorted_dict
info(f_sort_data_by_age(objects))

'''H. Create a function that takes a list of date objects and uses the sorted() function to return a new list 
with the dates sorted in chronological order.
'''
dates = [(2024, 10, 10), (1989, 10, 5), (2050, 3, 8), (2000, 12, 31), (2000, 11, 30)]
def f_sort_by_date(lst: list)-> list:
    date_data = lambda x: datetime.datetime(*x)
    sorted_dates = sorted(lst, key=date_data)
    return sorted_dates
info(f_sort_by_date(dates))

'''I. Implement a function that takes a list of lists and uses the sorted() function to return a new list with 
the lists sorted based on the sum of their elements.
'''
lsts = [
    [1, 2, 3, 4, 5],
    [1, 2],
    [1, 2, 3, 4, 5, 6, 7],
    [1, 2, 3],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
    [1]
]
def sort_by_list_length(lst: list) -> list:
    lst_length = lambda x: len(x)
    sorted_list = sorted(lst, key=lst_length)
    return sorted_list
info(sort_by_list_length(lsts))

'''J. Write a function that takes a list of integers and uses the sorted() function to return a new list with 
the integers sorted based on the number of factors they have.
'''
def f_factors_count(number: int) -> int:
    count = 2 # 1-e ve ozune bolunur
    for x in range(2, number // 2 + 1):
        if number % x == 0:
            count += 1
    return count 
numbers = [23, 345, 2, 5678, 987, 34, 987654, 76, 432]
def f_sort_by_factors_count(lst: list) -> list:
    return sorted(lst, key=f_factors_count)
info(f_sort_by_factors_count(numbers))

'''K. Create a function that takes a list of strings and uses the sorted() function to return a new list with 
the strings sorted based on their last characters.
'''
def f_sort_by_last_char(lst:list) -> list:
    return_last_char = lambda x: x[-1]
    return sorted(lst, key=lambda x: x[-1])
strings = 'strings sorted based on their last characters'.split()
info(f_sort_by_last_char(strings))

'''L. Implement a function that takes a list of dictionaries and uses the sorted() function to return a new list 
with the dictionaries sorted based on their keys.
'''
def f_sort_by_key(dictionary: dict) -> dict:
    sorted_keys = sorted(dictionary)
    sorted_dict = {}
    for x in sorted_keys:
        sorted_dict.update({x: dictionary.get(x) })
    return sorted_dict
my_dict = {
    'w':134,
    'b': 243,
    'k': 37,
    'a': 49
}

info(f_sort_by_key(my_dict))

'''M. Sort the following list of strings alphabetically by the second letter:
string_list = ["Hello", "World", "Python", "Programming", "Example", "String", "List", "ChatGPT"]
'''
string_list = ["Hello", "World", "Python", "Programming", "Example", "String", "List", "ChatGPT"]

find_second_letter = lambda x: x[1]
info(sorted(string_list, key=find_second_letter))

'''Quiz.
1. What is the purpose of the filter() function in Python?
    A) To remove elements from an iterable based on a given condition

2. Which of the following data types can the filter() function be applied to?
    D) All of the above

3. What does the filter() function return?
    A) A new iterable containing filtered elements

4. Which parameter does the filter() function take?
    C) Both A and B

5. In the context of the filter() function, what does the filter function do?
    A) Defines the condition for filtering elements

6. Which of the following statements is true about the filter() function?
    A) The filter function can only return True or False

7. What is the syntax for using the filter() function in Python?
    D) filter(iterable, function)

8. When using the filter() function, what happens if the filter function returns False for an element?
    D) None of the above

9. Can the filter() function be used to filter elements based on multiple conditions?
    A) Yes

10. In Python 3, what does the filter() function return by default?
    A) A filter object

11. What is the purpose of the map() function in Python?
    A) To apply a given function to each item in an iterable

12. Which of the following is an iterable that can be passed to the map() function?
    D) All of the above

13. What does the map() function return?
    A) A new iterable containing transformed elements

14. What parameters does the map() function take?
    D) A mapping function, followed by one or more iterables

15. In the context of the map() function, what does the mapping function do?
    A) Defines the transformation to be applied to each element

16. Which of the following is true about the map() function?
    A) The mapping function can return any data type

17. What is the syntax for using the map() function in Python?
    A) map(mapping_function, iterable)
    C) map(function, iterable)   

18. When using the map() function, what happens if the mapping function returns None for an element?
    A) The element is removed from the iterable

19. Can the map() function be used to transform elements from multiple iterables?
    A) Yes

20. In Python 3, what does the map() function return by default?
    A) A map object

21. What is the purpose of the reversed() function in Python?
    A) To reverse the order of elements in an iterable

22. Which of the following is an iterable that can be passed to the reversed() function?
    D) All of the above

23. What does the reversed() function return?
    A) A new iterable containing reversed elements

24. What parameter does the reversed() function take?
    A) An iterable

25. In the context of the reversed() function, what does "reversed elements" mean?
    A) The elements are in the opposite order

26. Which of the following is true about the reversed() function?
    C) The reversed elements are returned as an iterator

27. What is the syntax for using the reversed() function in Python?
    A) reversed(iterable)
    
8. When using the reversed() function, can it be applied to strings?
   A) Yes
   
9. Can the reversed() function be used to reverse a dictionary?
   A) Yes
   
0. In Python 3, what does the reversed() function return by default?
   A) A reversed object
   
1. What is the purpose of the sorted() function in Python?
   A) To sort elements in an iterable and return a sorted list

32. Which of the following is an iterable that can be passed to the sorted() function?
    D) All of the above
    
33. What does the sorted() function return?
    C) A list of sorted elements

34. What parameters does the sorted() function take?
    A) An iterable

35. In the context of the sorted() function, what does "sorted elements" mean?
    A) The elements are arranged in ascending order

36. Which of the following is true about the sorted() function?
    D) The sorted elements are returned as a list

37. What is the syntax for using the sorted() function in Python?
    D) sorted(iterable, function)

38. When using the sorted() function, can you specify a custom sorting order?
    A) Yes, by providing a custom sorting function

39. Can the sorted() function be used to sort a dictionary based on its keys or values?
    A) Yes

40. In Python 3, what does the sorted() function return by default?
    A) A list of sorted elements
    '''
