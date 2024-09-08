"""
- Tuples -
A. Create a tuple containing minimum seven different colors.
B. Create a tuple containing minimum five different countries.
C. Create a tuple containing three string values and two integer values.
D. Create a tuple containing all continents of the world.
E. Create a tuple containing minimum four car brands.
F. Create a tuple containing four different data types of Python.
G. Create a tuple containing only negative even numbers from -2 to -12.
H. Create a tuple containing only positive even numbers from 0 to 12.
I. Combine tuples from Task G and H.
J. Create a tuple containing minimum six students' names. Print the first
student's name.
K. Create a tuple containing three different integers. Print the integer
at position two.
L. Print the last element of Task D's tuple.
M. Print the last two elements of Task A's tuple. You can use slicing
method only once. Separately printing those elements will not be accepted.
N. Given the following tuple:
double_me = (0, 5, 10)

Create a new tuple containing the double value of that tuple.
O. Create any nested tuple. Print any value from the inner tuple and the whole
inner tuple.
P. Change the value of the color at position six of the tuple from Task A.
Q. From Task B's tuple print all countries except the first two.
R. Create two new tuples containing the double value of the tuple from Task F 
using 2 different mathematical operations.
S. Create an empty tuple.
T. Create a tuple with only the one 'Python' string value. Print its type.
U. Count how many times the word 'hacking' appears in this tuple:
black_hat = ('hacking', 'hiding', 'hiking', 'hacking', 'viking', 'horsing', 'black', 'hat', 'hacking')
V. Count how many 'True's are in this tuple:
booleans = (True, True, False, True, False, False, True)
W. Find the position of the first 'a' character in the following tuple:
randomized_alphabet = ('b', 'w', 'v', 't', 'n', 'c', 'd', 'a', 'f', 'a')
X. When should you consider using constant variables with tuples in your Python code? 
Provide an example scenario.

Bonus:
A. Print the whole tuple from previous tasks using the slicing method.
B. Print the length of any tuple from previous tasks.

- Sets -
You have the following set:
ages = {12, 14, 16, 18, 20, 22, 24, 26}
A. Write a Python program to remove an item from the 'ages' set if
it is present in the set.
B. Add 28 to 'ages' set.
C. Copy this set. Check if this copied set is a subset of the original set.
D. Check if the following set is a subset of the 'ages' set:
suspected_subset = {12, 14}
E. Remove 12 and 14 from the 'ages' set.
F. You have the following tuple and set:
names = ('Murad', 'Aysel', 'Gunel')
students = {'Bob', 'John'}

Extend the 'students' set with the 'names'.
G. Find the difference between the following sets:
fruits = {"apple", "banana", "cherry"}
items = {"google", "microsoft", "apple"}
H. Print the length of the 'ages' set. Then add 12 to the 'ages' set. Print the
length again.
I. Clear the 'ages' set. Print it and its length.

- Interview Questions -
A. Reverse a tuple with slicing method.
B. What's the main difference between Tuples and Lists in Python?
C. What's the best practice to use Sets, and not Lists or Tuples?
D. What's the difference between Set's 'remove' and 'discard' method?
E. You have the following list of the students of 7th grade class:
names = ["Murad", "Mike", "Murad", "Elcin", "Vuqar", "Murad", "Nargiz"]

How can you remove all duplicate names from this list?
F. When might you choose to use a set instead of a list or tuple in Python? 
Provide an example scenario.

- Comments -
A. One-line comment in any random three places of your code, if it's appropriate.
B. Multi-line comment anywhere in your code, if it's appropriate.

- Chat GPT's Homework -
A. Create a Python tuple named student_info that contains the following information about a student:
1. Student's name
2. Student's age
3. Student's grade (as a string, e.g., "A" or "B")
B. Create an empty list called shopping_cart. Then, perform the following operations:
1. Add three items to the shopping cart.
2. Remove one item from the shopping cart.
3. Modify one of the items in the shopping cart.
C. Create a tuple named coordinates containing latitude and longitude values. 
Then, use tuple unpacking (*) to assign these values to separate variables called latitude and longitude. 
Print the values of latitude and longitude.
D. Explain in your own words the main differences between tuples and lists in Python.
Provide examples of situations where you would use one over the other.

Quiz.
1. What is a tuple in Python?
    a) An ordered collection of elements that is mutable.
    b) An ordered collection of elements that is immutable.
    c) An unordered collection of elements that is mutable.
    d) An unordered collection of elements that is immutable.

2. How do you create an empty tuple in Python?
    a) empty_tuple = ()
    b) empty_tuple = []
    c) empty_tuple = {}
    d) empty_tuple = None
    e) empty_tuple = tuple()
    f) empty_tuple = tuple(list())

3. Question 3: Which of the following statements is true about sets in Python?
    a) Sets are ordered collections.
    b) Sets can contain duplicate elements.
    c) Sets are indexed using integers.
    d) Sets are mutable.
    
4. What is the primary purpose of using sets in Python?
    a) To store elements in a specific order.
    b) To ensure elements are unique and eliminate duplicates.
    c) To store data in an immutable form.
    d) To access elements using keys.   
    
5. Which of the following is true about the elements of a set in Python?
    a) Elements of a set are indexed.
    b) Elements of a set are ordered.
    c) Elements of a set must be of the same data type.
    d) Elements of a set can be of different data types.
    
6. What is the result of the following code?
    my_set = {1, 2, 3}
    my_set.add(4)
    my_set.remove(2)

    a) {1, 2, 3, 4}
    b) {1, 3, 4}
    c) {1, 2, 3}
    d) Error: 'remove' method does not exist for sets.    

7. Which of the following set operations returns the elements that are common to two sets?
    a) union()
    b) intersection()
    c) difference()
    d) symmetric_difference()

8. Can a tuple contain elements of different data types?
    a) Yes
    b) No      
    
9. What is the key difference between a tuple and a list in Python?
    a) Lists are immutable, and tuples are mutable.
    b) Lists are ordered and mutable, while tuples are ordered and immutable.
    c) Lists are unordered and mutable, while tuples are ordered and immutable.
    d) Lists can contain elements of different data types, but tuples cannot.
    
10. Which of the following is a valid way to create a set in Python?
    a) my_set = {1, 2, 3}
    b) my_set = [1, 2, 3]
    c) my_set = (1, 2, 3)
    d) my_set = "123"

11. Which of the following statements is true about tuples in Python?
    a) Tuples can be modified after creation.
    b) Tuples are indexed using integers.
    c) Tuples can contain duplicate elements.
    d) Tuples are unordered collections.

12. What is the advantage of using tuples over lists in Python?
    a) Tuples can be resized after creation.
    b) Tuples can contain elements of different data types.
    c) Tuples are faster for accessing elements.
    d) Tuples support list comprehension.

13. Which of the following list comprehensions creates a tuple of squares of numbers from 1 to 5?
    a) squared_tuple = (x ** 2 for x in range(1, 6))
    b) squared_tuple = [x ** 2 for x in range(1, 6)]
    c) squared_tuple = {x ** 2 for x in range(1, 6)}
    d) squared_tuple = (x ** 2 for x in [1, 2, 3, 4, 5])
    
14. What is the primary advantage of using sets when dealing with collections of data?
    a) Sets preserve the order of elements.
    b) Sets allow duplicate elements.
    c) Sets ensure elements are unique.
    d) Sets support indexing. 

15. In Python, what would be the result of applying the union() operation on two sets that 
have some overlapping elements?
    a) The operation will return the common elements.
    b) The operation will return all elements from both sets with duplicates removed.
    c) The operation will raise an error.
    d) The operation will return an empty set.   
    
16. How can you remove an item from a list without knowing its index?
    a) Using the remove() method.
    b) Using the pop() method.
    c) Using a for loop.
    d) You cannot remove an item without knowing its index.    

17. Which of the following statements is true about list comprehensions?
    a) List comprehensions can only be used with lists.
    b) List comprehensions are faster than for loops for creating lists.
    c) List comprehensions can only filter elements, not transform them.
    d) List comprehensions always create a new list.

18. What is the difference between the discard() and remove() methods for sets in Python?
    a) discard() removes an element if it exists; remove() raises an error if the element is not found.
    b) remove() removes an element if it exists; discard() returns the element if found.
    c) Both methods remove an element, but discard() is faster.
    d) There is no difference; discard() and remove() are interchangeable.
    
19. In Python, can a list contain elements of different data types?
    a) Yes
    b) No
    
20. In Python, what is a constant variable?
    a) A variable whose value can be changed during runtime.
    b) A variable used to store temporary data.
    c) A variable whose value should not change after it's initially assigned.
    d) A variable that can only store numerical values.

21. Which data structure in Python is commonly used to define constant variables?
    a) Lists
    b) Tuples
    c) Sets

22. How do you define a constant variable using a tuple in Python?
    a) constant_var = (value)
    b) constant_var = [value]
    c) constant_var = {value}
    d) constant_var = value

23. When defining constant variables using tuples, what is the recommended naming convention?
    a) Use lowercase letters with underscores (e.g., my_constant_var).
    b) Use uppercase letters with underscores (e.g., MY_CONSTANT_VAR).
    c) Use lowercase letters without underscores (e.g., myconstantvar).
    d) Use any naming convention as long as it's consistent.

24. Which of the following operations is valid for a constant variable defined using a tuple?
    a) Changing its value.
    b) Accessing its elements.
    c) Removing elements from it.
    d) Adding elements to it.

25. Why might you choose to use a constant variable defined with a tuple instead of a regular variable?
    a) To allow changes to the variable's value.
    b) To make the code less readable.
    c) To ensure that the variable's value remains constant.
    d) To allow the variable to store multiple values.

26. Which of the following code examples correctly defines a constant variable using a tuple?
    a) const_var = (3.14, 'hello', True)
    b) const_var = [3.14, 'hello', True]
    c) const_var = {3.14, 'hello', True}
    d) const_var = 3.14

27. What is the advantage of using constant variables with tuples over hardcoding values directly into your code?
    a) It allows for dynamic value changes.
    b) It improves code readability.
    c) It saves memory.
    d) It makes the code shorter.

28. In Python, can you reassign a value to a constant variable defined using a tuple?
    a) Yes
    b) No

29. What does the asterisk (*) operator do when used with a variable in Python?
    a) Multiplies the variable by itself.
    b) Raises the variable to the power of 2.
    c) Allows the variable to hold multiple values, like a list or tuple.
    d) Converts the variable to a string.

30. In Python, what does the from module_name import * statement do when importing a module?
    a) It imports all functions, classes, and variables from the module.
    b) It imports only the functions with names containing an asterisk () character.
    c) It imports nothing from the module.
    d) It raises a syntax error because the asterisk () is not allowed in import statements.

31. When might it be appropriate to use the asterisk () in a module import statement?
    a) When you want to import only a specific function from the module.
    b) When you want to import all contents of the module for convenience.
    c) When you want to create a new module with an asterisk () symbol in its name.
    d) When you want to prevent any imports from the module.
"""