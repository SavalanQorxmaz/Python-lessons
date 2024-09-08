# - Tuples -

colors = ('white', 'black', 'red', 'blue', 'green', 'yellow', 'gray', 'orange', 'violet')
countries = ('Azerbaijan', 'Turkiye', 'Italy', 'Ukrain', 'Russia', 'China', 'Singapur')
values = ('Country', 'City', 'Village', 27, 99)
continents = ('Asia', 'Africa', 'North America', 'South America', 'Antarctica', 'Europe', 'Australia')
cars = ('Audi', 'BMW', 'Tesla', 'Ferrari', 'Volvo')
data_types = (True, 32, 'String', [True, 32, 'String'])
negatives = (-12, -10, -8, -6, -4, -2)
positives = (0, 2, 4, 6, 8, 10, 12)
numbers = (-12, -10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10, 12 )
students = ('Ali', 'Murad', 'Leyla', 'Lale', 'Zahra', 'Fatma')
integers = (32, -100, 97)
print(integers[1])
print(continents[-1])   # L
print(colors[-2:])  # M
double_me = (0, 5, 10)  # N
doubled = tuple(x*2 for x in double_me)
print(doubled)
nested_tuple = (1, 5, 8, (23, 27, 29), 37, 45)  # O
print(nested_tuple[0])
print(nested_tuple[3][2])
colors_list = list(colors)  # P
colors_list[6] = 'changed_color'
colors = tuple(colors_list)
print(colors)
country1, country2, *rest_countries = countries # Q Method 1
print(rest_countries)
print(countries[2:])    # Method 2
data_types_list = []  # R
data_types_list = [x*2 for x in data_types] #  Method 1
data_types_double1 = tuple(data_types_list)
print(data_types_double1)
data_types_list.clear() # Method 2
for x in data_types:
    double_x = x * 2
    data_types_list.append(double_x)
data_types_double2  = tuple(data_types_list)
print(data_types_double2)
empty_tuple = ()    # S Method 1
empty_tuple2 = tuple()    # Method 2
my_tuple = ('Python',)  # T  
print(type(my_tuple))
black_hat = ('hacking', 'hiding', 'hiking', 'hacking', 'viking', 'horsing', 'black', 'hat', 'hacking')    # U
print(black_hat.count('hacking'))    # 3
booleans = (True, True, False, True, False, False, True)    # V
print(booleans.count(True))    # 4
randomized_alphabet = ('b', 'w', 'v', 't', 'n', 'c', 'd', 'a', 'f', 'a')    # W
print(randomized_alphabet.index('a'))    # 7
CONSTANT_POINTS = (1, 10, 100, 1000,)    # x

# Bonus:
print(colors[2:])
print(continents[:-1])
print(negatives[::-1])
print(positives[-1::-1])

print(len(colors))

# - Sets -
ages = {12, 14, 16, 18, 20, 22, 24, 26}
if 20 in ages:    # A
    ages.remove(20)
print(ages)
ages.add(28)    # B
print(ages)
ages_copy = ages.copy()    # C
issub = ages_copy.issubset(ages)
print(issub)
suspected_subset = {12, 14}    # D
issub = suspected_subset.issubset(ages)
print(issub)
ages.discard(12)    # E
ages.discard(14)
names = ('Murad', 'Aysel', 'Gunel')    # F
students = {'Bob', 'John'}
students.update(names)
print(students)
fruits = {"apple", "banana", "cherry"}    # G
items = {"google", "microsoft", "apple"}
dif = fruits.symmetric_difference(items)
print(dif)
print(f'before adding: {len(ages)}')    # H
ages.add(12)
print(f'After adding: {len(ages)}')
ages.clear()    # I
print(f'After cleaning: {len(ages)}')

# - Interview Questions -
my_tuple = (1, 2, 3, 4, 5)    # A
print(my_tuple)
temp_list = list(my_tuple)
temp_list.reverse()
my_tuple = tuple(temp_list)
print(my_tuple)
# B
''' List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 '''
# C
'''
Duplicate member not allowed
'''
# D
'''
If the item to remove does not exist, discard() will NOT raise an error.
If the item to remove does not exist, remove() will raise an error.
'''
names = ["Murad", "Mike", "Murad", "Elcin", "Vuqar", "Murad", "Nargiz"]    # E
print(names)
temp_set = set(names)
names = list(temp_set)
print(names)
#  F
'''if we need non dublicated data:
'''

# - Chat GPT's Homework -
student_info = ('Ali', 25, 'B')   # A
shopping_cart = []    # B
shopping_cart.extend(('Phone', 'Parfume', 'Shoes'))
print(f'After add elements: {shopping_cart}')
shopping_cart.remove('Parfume')
print(f'After remove element: {shopping_cart}')
shopping_cart[0] = 'Computer'
print(f'After modify element: {shopping_cart}')
coordinates = (41.2, 40.21)    # C
(latitude, longitude) = coordinates
print(f'Latitude: {latitude}\nLongtitude: {longitude}')
# D
'''
If we need data keep unchangeable,we need use tuple, but list changeable
'''
# Quiz.
'''
1. What is a tuple in Python?
    b) An ordered collection of elements that is immutable.

2. How do you create an empty tuple in Python?
    a) empty_tuple = ()
    e) empty_tuple = tuple()

3. Question 3: Which of the following statements is true about sets in Python?
    c) Sets are indexed using integers.
    
4. What is the primary purpose of using sets in Python?
    b) To ensure elements are unique and eliminate duplicates.
    
5. Which of the following is true about the elements of a set in Python?
    d) Elements of a set can be of different data types.
    
6. What is the result of the following code?
    my_set = {1, 2, 3}
    my_set.add(4)
    my_set.remove(2)

    b) {1, 3, 4}  

7. Which of the following set operations returns the elements that are common to two sets?
    b) intersection()

8. Can a tuple contain elements of different data types?
    a) Yes     
    
9. What is the key difference between a tuple and a list in Python?
    b) Lists are ordered and mutable, while tuples are ordered and immutable.
    
10. Which of the following is a valid way to create a set in Python?
    a) my_set = {1, 2, 3}

11. Which of the following statements is true about tuples in Python?
    c) Tuples can contain duplicate elements.

12. What is the advantage of using tuples over lists in Python?
    c) Tuples are faster for accessing elements.

13. Which of the following list comprehensions creates a tuple of squares of numbers from 1 to 5?
    a) squared_tuple = (x ** 2 for x in range(1, 6))
    
14. What is the primary advantage of using sets when dealing with collections of data?
    c) Sets ensure elements are unique.

15. In Python, what would be the result of applying the union() operation on two sets that 
have some overlapping elements?
    b) The operation will return all elements from both sets with duplicates removed.
    
16. How can you remove an item from a list without knowing its index?
    a) Using the remove() method.

17. Which of the following statements is true about list comprehensions?
    b) List comprehensions are faster than for loops for creating lists.
    d) List comprehensions always create a new list.

18. What is the difference between the discard() and remove() methods for sets in Python?
    a) discard() removes an element if it exists; remove() raises an error if the element is not found.
    
19. In Python, can a list contain elements of different data types?
    a) Yes
    
20. In Python, what is a constant variable?
    c) A variable whose value should not change after it's initially assigned.

21. Which data structure in Python is commonly used to define constant variables?
    b) Tuples

22. How do you define a constant variable using a tuple in Python?
    d) constant_var = value

23. When defining constant variables using tuples, what is the recommended naming convention?
    b) Use uppercase letters with underscores (e.g., MY_CONSTANT_VAR).

24. Which of the following operations is valid for a constant variable defined using a tuple?
    b) Accessing its elements.

25. Why might you choose to use a constant variable defined with a tuple instead of a regular variable?
    c) To ensure that the variable's value remains constant.

26. Which of the following code examples correctly defines a constant variable using a tuple?
    a) const_var = (3.14, 'hello', True)

27. What is the advantage of using constant variables with tuples over hardcoding values directly into your code?
    b) It improves code readability.

28. In Python, can you reassign a value to a constant variable defined using a tuple?
    b) No

29. What does the asterisk (*) operator do when used with a variable in Python?
    c) Allows the variable to hold multiple values, like a list or tuple.

30. In Python, what does the from module_name import * statement do when importing a module?
    a) It imports all functions, classes, and variables from the module.

31. When might it be appropriate to use the asterisk () in a module import statement?
    b) When you want to import all contents of the module for convenience.
'''




