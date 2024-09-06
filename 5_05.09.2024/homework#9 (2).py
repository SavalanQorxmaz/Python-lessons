"""
- Lists -
A. Create an empty list and add 5 user-input integers to it.
B. Take a list of integers as input and print the sum of all the elements in the list.
C. Ask the user for a sentence and store each word as an element in a list.
D. Write a program that asks user for six countries. The program should create a list of
those countries and ask for three countries to delete from the list. Make the program
user-friendly, and print each time the content of a list to show the user which countries
are in a list.
E. Which list method makes any list look the same. The lists are the same if its content,
elements and all other properties are the same.
F. Create an empty list and print its length.
Write a function that accepts a list of names and returns the name with the longest length.
G. Ask the user for a list of integers and find the second-largest number in the list.
H. Ask the user for a list of integers and find the mean value of that list.
I. Ask the user for a list of integers and find the third-smallest number in the list.
J. Write a program that asks the user for three colors separated by spaces. The
program should print all those colors using comma (you should use string 'join' method). 
For example:
Your colors are red, blue, white.

K. Write a program that asks the user for four capital cities separated by spaces. 
The program should print all those cities the following structure:
There are many capital cities in the world. For example, Baku, Moscow and Kyiv.

You should follow all instructions, and not make changes to the structure of final sentence.
L. Take a list of strings as input and sort it in alphabetical order.
M. Take a list of numeric values as input and sort it in descending order.
N. Remove duplicates from a list entered by the user while preserving the original order.
O. Write a program that accepts two lists and concatenates them into a single list.
The first list is a list of fruits, the second is a list of vegetables.
P. Write a program that prints 'True' if there is at least one item in a 'my_list' list.

- List Comprehension -
Suppose you have the following lists:
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
letters = ['p', 'y', 't', 'h', 'o', 'n']
times = [1, 2, 3, 4, 5]

A. Create a list containing raised to power two values of 'digits' list.
B. Create a list containing capitalized version of letter values of 'letters' list.
C. Create a list containing the 'Comprehension' string value the amount of 'times'
list's length time.
D. Create a list containing 5 random integers between -5 and 5. find the second-smallest 
number in the list. The program should print 'True' if that number is negative, and 'False'
otherwise.
E. Create a list of 10 random numbers and find the maximum and minimum values.

- Comments -
A. One-line comment, if it's appropriate.
B. Multi-line comment, if it's appropriate.

- Chat GPT's Homework -
A. Create a list of colors and write a function that duplicates each color in the 
list. For example, if the list contains "red," it should become ["red", "red"]. 
Print the modified list.
B. How many methods do you know to create an empty list in Python? 
C. Which list method is used to add an element to the end of a list?
D. Write a Python code snippet to access the third element in a list named my_list. 
E. Which list method is used to remove the last element from a list? 
F. What list method is used to insert an element at a specific position? 
G. Write Python code to reverse a list called my_list in-place. 
H. How can you create a shallow copy of a list in Python? 
I. Which list method is used to count the number of occurrences of a specific element in a list? 
J. Write a Python code snippet to concatenate two lists, list1 and list2. 
K. What list method can be used to sort a list in ascending order? 
L. Write Python code to remove the first occurrence of an element 'x' from a list. 
M. Explain the difference between append() and extend() methods when adding elements to a list. 
N. Which list method can be used to remove all elements from a list? 
O. Write Python code to find the index of the first occurrence of an element 'x' in a list. 
P. What list method can be used to remove and return an element from a specific index in a list?

Quiz.
1. Which method is used to add an element to the end of a list in Python?
    a) add()
    b) insert()
    c) extend()
    d) append()

2. What is the purpose of the insert() method for lists in Python?
    a) Remove an element from a list.
    b) Add an element to the beginning of a list.
    c) Add an element at a specific index in the list.
    d) Replace an element at a specific index in the list.

3. Which list method is used to remove and return the last element of a list?
    a) pop()
    b) remove()
    c) delete()
    d) discard()    

4. What does the extend() method do when used on a list in Python?
    a) Adds an element to the beginning of the list.
    b) Adds a new list as elements to the existing list.
    c) Removes the last element from the list.
    d) Sorts the list in ascending order.

5. Which list method is used to reverse the order of elements in a list in Python?
    a) reverse()
    b) flip()
    c) backwards()
    d) revert()

6. What does the sort() method do when used on a list in Python?
    a) Reverses the order of elements in the list.
    b) Removes all elements from the list.
    c) Sorts the list in ascending order.
    d) Sorts the list in descending order.

7. Which method is used to find the index of the first occurrence of an element in a list?
    a) index()
    b) find()
    c) search()
    d) lookup()

8. What is the purpose of the pop() method when used on a list in Python?
    a) Adds an element to the end of the list.
    b) Removes and returns the last element of the list.
    c) Removes the first element of the list.
    d) Inserts an element at a specific index in the list.

9. How can you count the number of occurrences of a specific element in a list?
    a) Use the count() method.
    b) Use the occurrences() method.
    c) Use the find_count() method.
    d) Use the search_count() method.

10. How can you check if a list is empty in Python?
    a) Use the empty() method.
    b) Use the is_empty() method.
    c) Use the len() function and check if it's equal to zero.
    d) Use the has_elements() method.

11. Which method is used to copy the elements of one list to another in Python?
    a) copy()
    b) duplicate()
    c) clone()
    d) replicate()

12. How do you remove an element by index from a list in Python?
    a) Use the remove() method with the index as an argument.
    b) Use the pop() method with the index as an argument.
    c) Use the delete() method with the index as an argument.
    d) Use the discard() method with the index as an argument.

13. What does the len() method do when applied to a list?
    a) Returns the maximum value in the list
    b) Returns the minimum value in the list
    c) Returns the number of elements in the list
    d) Returns the sum of all elements in the list

14. Given the following list, what is the output of min(my_list)?
    my_list = [0, 2, 4, 1, 5]
    result = min(my_list)

    a) 0
    b) 1
    c) 4
    d) 5

15. Given the following list, what is the output of max(my_list)?
    my_list = [0, 2, 4, 1, 5]

    a) 0
    b) 1
    c) 4
    d) 5

16. Which list method can be used to find the number of occurrences 
of a specific element in a list?
    a) count()
    b) len()
    c) sum()
    d) max()

17. What is the output of the following code snippet?
    my_list = [1, 2, 3, 4, 5]
    my_list.reverse()
    print(my_list)

    a) [1, 2, 3, 4, 5]
    b) [5, 4, 3, 2, 1]
    c) [1, 2, 3, 4]
    d) [5, 4, 3, 2]

18. What is the output of the following code snippet? 
    my_list = [1, 2, 3] 
    my_list.insert(1, 4) 
    print(my_list)

    a) [1, 2, 3] 
    b) [1, 4, 2, 3] 
    c) [4, 1, 2, 3] 
    d) [1, 2, 4, 3] 

19. Which method is used to remove all elements from a list? 
    a) clear() 
    b) remove_all() 
    c) delete_all() 
    d) reset() 

20. What is the output of the following code snippet? 
    my_list = [1, 2, 3, 4, 5] 
    result = sum(my_list) 
    print(result)

    a) 15 
    b) [1, 2, 3, 4, 5] 
    c) [5, 4, 3, 2, 1] 
    d) 10 

21. What is the output of the following code snippet? 
    my_list = [1, 2, 3, 4, 5] 
    result = my_list.index(3) 
    print(result)

    a) 0 
    b) 1 
    c) 2 
    d) 3
"""