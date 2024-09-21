"""
- For Loops -
A. Write a program that uses a for loop to iterate over the numbers 
from 1 to 10 (inclusive) using the range method. Print each number.
B. Create a list of fruits with at least 5 fruits. Use a for loop to 
iterate over the list and print each fruit.
C. Write a program that takes a string input from the user and uses a 
for loop to iterate over the characters in the string. Print each character.
D. Create a dictionary with at least 3 key-value pairs where keys are names 
and values are ages. Use a for loop to iterate over the dictionary and print 
each name and age pair.
E. Create a list of dictionaries where each dictionary represents a person 
with a name and an age. Use a for loop to iterate over the list and print
the name and age of each person.
F. Write a program that calculates and prints the factorial of a number 
entered by the user. Use a for loop.
G. Write a program that takes a number from the user and prints a pattern using 
a for loop. For example, if the user enters 5, the output should be:
*
**
***
****
*****
H. Write a program that takes a list of numbers as input from the user 
and uses a for loop to find and print the sum of all even numbers in the list.
I. What is the purpose of a for loop in Python, and how is it different from a while loop?
J. Write a Python for loop that prints the numbers from 1 to 5 (inclusive).
K. Given a list of names: names = ['Alice', 'Bob', 'Charlie', 'David'], write a Python for 
loop to print each name.
L. Using a for loop, calculate the sum of all odd numbers from 1 to 10 (inclusive).
M. Explain the concept of iterating over a string using a for loop. Provide a Python 
code snippet that demonstrates this concept.
N. Write a Python for loop that iterates over a range of numbers from 1 to 10 (inclusive) 
and prints the square of each number.
O. You have the following tuple:
numbers = (10, 20, 30, 40, 50)

Iterate over this tuple and print the number if it's above 25.
P. Write a program that uses a for loop to find and print the largest number in a given list.
Don't use 'max' method.
Q. Write a Python program that uses a for loop to print the multiplication table (up to 10) 
for a given number.

Quiz.
1. Consider the following Python code:
    for i in range(5):
        print(i)

    What will be the output of this code?
    a) 0 1 2 3 4
    b) 1 2 3 4 5
    c) 0 1 2 3
    d) 1 2 3 4

2. Consider the following Python code:
    total = 0
    for i in range(1, 6):
        total += i
    print(total)

    What will be the output of this code?
    a) 15
    b) 10
    c) 5
    d) 20

3. Consider the following Python code:
    numbers = [10, 20, 30, 40, 50]
    for num in numbers:
        print(num)

    What will be the output of this code?
    a) 10 20 30 40 50
    b) 50 40 30 20 10
    c) 10 11 12 13 14
    d) 1 2 3 4 5

4. Consider the following Python code:
    word = "Python"
    for char in word:
        print(char * 3)

    What will be the output of this code?
    a) PPPyyyttthhhooonnn
    b) Pyytthhoonn
    c) Python
    d) PPyytthhoonn

5. How do you define a for loop in Python?  
    a) for i in range(n):
    b) for i in n:
    c) for i = 0 to n:
    d) for i = 0; i < n; i++:

6. What will the following code output?
    numbers = [1, 2, 3, 4, 5]
    for num in numbers:
        print(num * 2)

    a) 1 2 3 4 5
    b) 2 4 6 8 10
    c) 0 1 2 3 4
    d) 1 4 9 16 25

7. How do you iterate over a dictionary using a for loop in Python?
    a) for key in dictionary:
    b) for value in dictionary:
    c) for key, value in dictionary.items():
    d) for item in dictionary.items():

8. What is the range function used for in a for loop?
    a) To generate a sequence of numbers
    b) To calculate the sum of numbers
    c) To determine the length of a sequence
    d) To sort a sequence of numbers

9. What is the correct way to nest for loops in Python?
    a) By placing one for loop inside another
    b) By separating for loops with a comma
    c) By using a while loop within a for loop
    d) By using a break statement inside a for loop

10. In Python, what is the output of the following loop?
    for i in range(3):
        print(i, end=' ')

    a) 0 1 2
    b) 1 2 3
    c) 0 1 2 3
    d) 3 2 1 0

11. Which of the following statements is true about the range function in Python?
    a) It generates a sequence of numbers.
    b) It returns a list.
    c) It generates random numbers.
    d) It is used to calculate the average of a sequence.

12. In Python, how do you iterate through a list in reverse order using a for loop?
    a) for i in reversed(list):
    b) for i in range(len(list), -1, -1):
    c) for i in range(len(list) - 1, -1, -1):
    d) for i in list[::-1]:

13. Which of the following data types can you iterate over using a for loop in Python?
    a) String
    b) Integer
    c) Boolean
    d) None

14. What is the correct syntax for a nested for loop in Python?
    a)
    for i in range(5):
        for j in range(3):
            print(i, j)
    b)
    for i in range(5) and j in range(3):
        print(i, j)
    c)
    for i in range(5):
        print(i)
    for j in range(3):
        print(j)
    d)
    for i in range(5):
        for j in range(3):
        print(i, j)

15. In Python, what is immutability?
    a) The ability of an object to be changed after it is created
    b) The inability of an object to be changed after it is created
    c) The ability of an object to be resized
    d) The ability to store mutable objects

16. Which of the following data types in Python is immutable?
    a) Lists
    b) Tuples
    c) Dictionaries
    d) Sets
        
17. What is the primary difference between a tuple and a list in Python?
    a) Tuples are mutable, and lists are immutable
    b) Tuples can contain elements of different data types, while lists cannot
    c) Tuples are ordered, and lists are unordered
    d) Tuples are immutable, and lists are mutable

18. What is an iterable in Python?
    a) An object that cannot be iterated over
    b) An object that can be modified
    c) An object that can be looped over using a for loop
    d) An object that can be resized

19. Which of the following is NOT an example of an iterable in Python?
    a) String
    b) Integer
    c) List
    d) Tuple

20. What is the purpose of the iter() function in Python?
    a) It creates an iterator object for an iterable
    b) It converts an iterable to a list
    c) It checks if an object is iterable
    d) It reverses the elements of an iterable

21. Which method is used to advance an iterator in Python?
    a) next()
    b) advance()
    c) move()
    d) iterate()

22. What is the purpose of the next() function in Python?
    a) It retrieves the next element from an iterator
    b) It returns a list of all elements in an iterator
    c) It reverses the order of elements in an iterator
    d) It checks if an object is an iterator

23. Which exception is raised when the next() function is called on an exhausted iterator in Python?
    a) StopIteration
    b) IteratorError
    c) ValueError
    d) IterationError

24. What will the following code output?
    my_list = [1, 2, 3, 4, 5]
    my_iterator = iter(my_list)
    print(next(my_iterator))
    print(next(my_iterator))
    print(next(my_iterator))
    print(next(my_iterator))
    print(next(my_iterator))

    a) 1 2 3 4 5
    b) 1 2 3 4
    c) 1 2 3
    d) 1 1 1 1 1        

25. What is the correct way to use a for loop with an iterator in Python?
    a) Use for element in iterator:
    b) Use for element in iter(iterator):
    c) Use for element in next(iterator):
    d) Use for element in iterator.next():

26. How can you use a for loop to iterate a specific number of times and prompt 
the user for input within the loop?
    a)
    for i in range(5):
        user_input = input("Enter a value: ")
    b)
    for user_input in range(5):
        user_input = input("Enter a value: ")
    c)
    for i in range(int(input("Enter the number of times: "))):
        user_input = input("Enter a value: ")
    d)
    for i in input("Enter the number of times: "):
        user_input = input("Enter a value: ")

27. How can you use a for loop to iterate over a list of names and print 
a customized greeting based on each name?
    a)
    names = ['Alice', 'Bob', 'Charlie']
    for name in names:
        print("Hello, " + name + "!")
    b)
    names = ['Alice', 'Bob', 'Charlie']
    for name in range(len(names)):
        print("Hello, " + names[name] + "!")
    c)
    names = ['Alice', 'Bob', 'Charlie']
    for i in range(len(names)):
        print("Hello, " + i + "!")
    d)
    names = ['Alice', 'Bob', 'Charlie']
    for name in names:
        print("Hello, names!")

28. How can you use an if statement within a for loop to 
print even numbers from a given range?
    a)
    for i in range(10):
        if i % 2 == 0:
            print(i)
    b)
    for i in range(10):
        if i % 2:
            print(i)
    c)
    for i in range(10):
        if i / 2 == 0:
            print(i)
    d)
    for i in range(10):
        if i % 2 != 0:
            print(i)
"""