
# - For Loops -
'''A. Write a program that prints "Python" four times in a row.
'''
word = 'Python'
for i in range(4):
    print(word, end=' ')
print()
    

'''B. Write a program that prints "Python" four times in one row. Expected output:
PythonPythonPythonPython
'''
word = 'Python'
for i in range(4):
    print(word, end='')
print()

'''C. Write a program that prints numbers from 0 to 7.
'''
for i in range(8):
    print(i)

'''D. Write a program that asks the user how many time the phrase should
be printed. Depending on that input the program should print prints the
"Loops are very good" phrase.
'''
# how_many = int(input('how many time the phrase should be printed: '))
# for i in range(how_many):
#     print('Loops are very good')

'''E. Using f-strings and looping five times print the following output:
Looping No.1
Looping No.2
Looping No.3
Looping No.4
Looping No.5
'''
for i in range(5):
    print(f'Looping No.{i}')

'''F. Write a program that asks user for six student name. Add those names
to a list. Then print their name with corresponding order number. Ex. o.:
1. Leyla
2. Aysel
3. Gunel
4. Murad
5. Mark
6. John
'''
print('six student')
students = [ ]
for i in range(6):
    student = input('Student: ')
    students.append(student)
for n, student in enumerate(students, 1):
    print(f'{n}. {student}')

# - Chat GPT's Homework -
'''1. Write a program that uses a for loop to print the numbers from 1 to 10.
'''
for i in range(1, 11):
    print(i)

'''2. Write a program that calculates and prints the sum of all numbers from 1 to 100 using a for loop.
'''
print('sum of all numbers from 1 to 100')
sum = 0
for i in range(1, 101):
    sum += i
print(sum)

'''3. Write a program that takes an integer input from the user and uses a for loop to print the multiplication table for that number up to 10.
'''
print('multiplication table')
number = int(input('Number: '))
for i in range(11):
    print(number * i)

'''4. Write a program that takes a string input from the user and uses a for loop to count and print the number of characters in the string.
'''
print('for loop to count')
word = input('Word or sentence:')
for n, x in enumerate(word):
    print(n)

'''5. Write a program that takes a string input from the user and uses a for loop to print the characters of the string in reverse order.
'''
print('string in reverse order')
word = input('Word or sentence: ')
for x in word[::-1]:
    print(x)

'''6. Write a program that takes an integer input from the user and uses a for loop to calculate and print the factorial of that number.
'''
print('factorial of number')
fact = 1
number = int(input('Number: '))
for i in range(1, number + 1):
    fact *= i
print(f'{number}! = {fact}')

'''7. Write a program that takes an integer input from the user and uses a for loop to print a table of powers for that number up to the 5th power.
'''
print('up to the 5th power')
number = int(input('Number: '))
for i in range(1, 6):
    print(number**i)

# Quiz.
# 1. What is the purpose of loops in programming?
#     b) To repeat a block of code multiple times

# 2. Which type of loop is commonly used to repeat a block of code a fixed number of times?
#     b) for loop

# 3. How is the range() function used in a for loop?
#     b) It creates a list of numbers in a given range

# 4. What's a scenario in real life that can be likened to a loop in programming?
#     a) Listening to a song on repeat

# 5. Which of the following code snippets will print "Hello, Loop!" five times?
#     a) 
#   for i in range(5):
#         print("Hello, Loop!")
    # b) 
#   for i in range(1, 6):
#         print("Hello, Loop!")
    # d) 
#   for i in range(5, 0, -1):
#         print("Hello, Loop!")

# 6. What will the following code snippet print?
#     for i in range(3):
#         print("*" * (i + 1))

#     a)
#     *
#     **
#     ***

# 7. Loops are essential in programming because they help to:
#     b) Repeat code without any restrictions

# 8. Which of the following options correctly describes an infinite loop?
#     d) A loop that continues running endlessly

# 9. What does the range() function return?
#     a) A list of numbers

# 10. Which of the following is NOT an iterable that can be used with a for loop?
#     d) Integers
# #