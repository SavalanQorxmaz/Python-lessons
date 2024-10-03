from lorem_text import lorem
import random
import string
# Note. Use the with keyword to open and close the file, ensuring proper file handling.

# - Working with Files -
'''A. Write a program to read an entire text file. The name of a file should 
be given by a user.
'''
file_name = f'{input('File.name without extension: ')}.txt'
file = open(file_name, 'w')
file_text = input('File text: ')
file.write(file_text)
try:
    file = open(file_name, 'r')
except FileNotFoundError:
    print('File not found')
else:
    print(file.read())
    file.close()

'''B. Write a program to read first n lines of a file.
'''
try:
    file = open('salam.txt', 'r')
except FileNotFoundError:
    print('file not found')
else:
    print(file.readline())
    file.close()

'''C. Write a program to read last n lines of a file.
'''
with open('my_file.txt', 'w') as file:
    for i in range(20):
        file.write(f'Line {i+1}\n')

try:
    file = open('my_file.txt', 'r')
    lst = file.readlines()
    length = len(lst)
    for i in range(length):
        if i < 10:
            print(lst[length-1-i])
except FileNotFoundError:
    print('File not found')
      
    

'''D. Write a program to read a file line by line and store it into a list.
'''
lst = [ ]
try:
    with open('my_file.txt', 'r') as my_file:
        for line in my_file.readlines():
            lst.append(line.split('\n')[0])
except FileNotFoundError:
    print('File not found')
else:
    print(lst)

'''E. Write a program to read a file line by line store it into a variable.
'''
var = ''
try:
    file = open('my_file.txt', 'r')
    length = len(file.readlines())
    file.close()
except FileNotFoundError:
    print('File not found')
else:
    file = open('my_file.txt', 'r')
    for x in range(length):
        var += ' ' + file.readline()
    print(f'var: {var}')


'''F. Write a python program to find the longest words.
'''

try:
    with open('lorem.txt', 'w+') as my_text:
        text = lorem.sentence()
        my_text.write(text)
except FileNotFoundError:
    print('File not found')
else:
    longest_word = ''
    file = open('lorem.txt', 'r')
    for x in file.read().split():
        if len(x) > len(longest_word):
            longest_word = x
    print(longest_word)
    

'''G. Write a Python program to count the number of lines in a text file.
'''
try:
    file = open('my_file.txt', 'r')
    length = len(file.readlines())
    file.close()
except FileNotFoundError:
    print('File not found')
else:
    print(length)

'''H. Write a Python program to count the frequency of words in a file.
'''
try:
    file = open('lorem.txt', 'r')
    text = file.read()
    text_array = text.split()
    count = len(text_array)
    print(count)
except FileNotFoundError:
    print('File not found')

'''I. Write a Python program to write a list to a file.
'''
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
try:
    with open('list.txt', 'w') as file:
        for x in lst:
            file.write(f'{x}\n')
except ValueError as err:
    print(err)
else:
    file = open('list.txt', 'r')
    print(file.read())
    file.close()

'''J. Write a Python program to combine each line from first file with the corresponding line in second file.
'''
first_file = open('first_file.txt', 'w')
lst1 = [f'{i}' for i in range(1, 31)]
print(lst1)
for x in lst1:
    first_file.write(f'{x}\n')
first_file.close()
second_file = open('second_file.txt', 'w')
lst2 = [f'{i}' for i in range(31,61)]
print(lst2)
for x in lst2:
    second_file.write(f'{x}\n')
second_file.close()
try:
    first_file = open('first_file.txt', 'r')
    second_file = open('second_file.txt', 'r')
    second_lst = [f'{x.split('\n')[0]}' for x in second_file.readlines()]
    print(second_lst)
    second_file.close()
    try:  
        second_file = open('second_file.txt', 'w')
        for z in second_lst:
            second_file.write(f'{first_file.readline().split('\n')[0]}--- {z}\n')
    except FileNotFoundError:
        print('File not found')
    else:
        second_file.close()
    
except FileNotFoundError:
    print('File not found')
else:
    first_file.close()


'''K. Write a program that combines two different file contents with titles ("File No.1", "File No.2")
before the content of each file
'''
try:
    first_file = open('first_file.txt', 'r')
    first = first_file.read()
    second_file = open('second_file.txt', 'r')
    second = second_file.read()
    text = f'File No.1\n{first}\nFile No.2\n{second}'
except FileNotFoundError:
    print('file not found')
else:
    print(text)

'''L. Write a Python program to read a random line from a file.
'''
try:
    my_file = open('my_file.txt', 'r')
    text = random.choice(my_file.readlines())
    my_file.close()
except FileNotFoundError:
    print('File not found')
else:
    print(text)
    
    
'''M. Write a Python program to assess if a file is closed or not.
'''
file = open('new_file.txt', 'w')
file.write('New file')
file.close()
try:
    if file.closed:
        print('File close')
    else:
        print('file open, access denied')
except FileNotFoundError:
    print('File not found')
    



'''N. Write a Python program to create a file where all letters of English alphabet are listed 
by specified number of letters on each line. Output:
ABC
DEF
GHI
JKL
MNO
PQR
STU
VWX
YZ
'''
letters = [x for x in string.ascii_uppercase]
print(letters)
letters_file = open('letters.txt', 'w')
while len(letters) > 0:
    letters_file.write(f'{''.join(letters[0:3])}\n')
    letters = letters[3:]
letters_file.close()


'''O. Suppose you have the following list:
filenames = [
    "bill.pdf",
    "invoice.pdf",
    "registration.pdf",
    "certificate.pdf"
]
Write a program that creates all those files.
'''
filenames = [
    "bill.pdf",
    "invoice.pdf",
    "registration.pdf",
    "certificate.pdf"
]

for x in filenames:
    file = open(f'{x}', 'w')
    file.write(x)
    file.close()

# - Chat GPT's Homework -

'''Task 1. Create a text file named "students.txt" with the names of five students, 
one name per line.
'''
students = ['Lale', 'Leyla', 'Aysel', 'Ayten', 'Ayshen']
file = open('students.txt', 'w')
for x in students:
    file.write(f'{x}\n')
file.close()

'''Task 2. Write a Python program that reads the contents of the "students.txt" file 
using the 'r' mode and prints each student's name on a separate line.
'''
try:
    file = open('students.txt', 'r')
    for i in range(len(students)):
        print(file.readline())
except FileNotFoundError:
    print('File not found')
else:
        file.close()

'''Task 3. Add a function to your program that allows the user to input the name of a
new student. Append this name to the "students.txt" file using the 'a' mode. 
Ensure that the name is written on a new line.
'''
try:
    file = open('students.txt', 'a')
    file.write(input('New student: ').capitalize())
    file.close()
except FileNotFoundError:
    print('File not found')

'''Task 4. Implement a feature that lets the user update a student's name. Ask the 
user to input the old name of the student they want to update and the new name. 
Update the "students.txt" file accordingly. Make sure to handle cases where 
the student's name may appear more than once.
'''
try:
    file = open('students.txt', 'r')
    students = [student.split('\n')[0].lower() for student in file.readlines()]
    file.close()
except FileNotFoundError:
    print('File not found')
else:
    current = input('Current student: ').strip().lower()
    new = input('New student: ').strip().lower()
    students[students.index(current)] = new
    students = [f'{student.capitalize()}\n' for student in students]
    file = open('students.txt', 'w')
    file.write(''.join(students))
    file.close()

'''Task 5. After each operation (reading, adding, updating), display the updated 
list of students to the user.
'''
try:
    file = open('students.txt', 'r')
    print(file.read())
    file.close()
except FileNotFoundError:
    print('File not found')

'''Task 6. Allow the user to search for a student's name in the list and display 
whether or not the student is present in the file.
'''
try:
    file = open('students.txt', 'r')
    students = [student.split('\n')[0].lower() for student in file.readlines()]
    file.close()
except FileNotFoundError:
    print('File not found')
else:
    search = input('Search student: ').strip().lower()
    try:
        index = students.index(search)
        print(f'User index: {index+1}')
    except ValueError:
        print(f'{search} Not in the list')

# Quiz.
# 1. What is the primary purpose of using the with statement (with context 
# manager) when working with files in Python?
#     c) To ensure proper file handling by automatically opening and closing the file.

# 2. What are the benefits of using the with statement for file handling in Python?
#     c) It automatically opens and closes the file.

# 3. What can happen if you don't close files before exiting a Python program?
#     a) It can lead to a memory leak.

# 4. Why is it important to close files after you're done with them in a Python program?
#     a) To free up system resources.
#     d) To ensure that the file is read-only.

# 5. Which file mode is used for reading a file in Python?
#     a) 'r'

# 6. What keyword is used to ensure proper file handling, automatically 
# closing the file when done?
#     c) with

# 7. What mode should you use to open a file for writing, and create a new 
# file if it doesn't exist, or truncate the file if it exists?
#     c) 'w'

# 8. How can you read the entire content of a file and store it as a string in Python?
#     c) Using the read() method

# 9. What file mode should you use to add new data to an existing file 
# without overwriting its content?
#     b) 'a'

# 10. Which of the following Python code snippets correctly opens a file 
# in read mode, reads its contents line by line, and prints them?
#     c)
#     file = open("data.txt", "r")
#     lines = file.readlines()
#     for line in lines:
#         print(line)

# 11. How can you add a new line of text to an existing file in Python 
# without overwriting its existing content?
#     c) Open the file in 'a' mode and write the new line of text.

# 12. To update a specific piece of data within an existing file, you should:
#     c) Read the entire file, modify the data in memory, and rewrite the entire file.

# 13. Which of the following is a good practice when working with files in Python
#     b) Using the try...except statement without handling file exceptions.

# 14. What does the 'x' mode do when opening a file?

# 15. What does the following code snippet do?
#     with open("file.txt", "w") as file:
#         file.write("Hello, World!")

#     b) Opens the file "file.txt" for writing and overwrites its content with "Hello, World!".

# 16. If you want to read the first 100 characters from a file named "data.txt" 
# and store them in a variable, which code snippet should you use?
#     b)
#     with open("data.txt", "r") as file:
#         data = file.read()
#         data = data[:100]

# 17. What will the following code snippet do?
#     with open("file.txt", "a") as file:
#         file.write("Line 1\nLine 2\nLine 3")

#     b) Appends three lines to the end of the file: "Line 1", "Line 2", and "Line 3".
# 18. What is the purpose of the 'b' mode when opening a file in Python?
#     a) Opens the file for binary read/write operations.

# 19. What does the following code snippet do?
#     with open("data.txt", "r") as file:
#         lines = file.readlines()
#         for line in lines:
#             print(line.strip())

#     c) Reads all lines from the file "data.txt" and prints them without trailing newline characters.

# 20. What does the following code snippet do?
#     with open("grades.txt", "r") as file:
#         total = 0
#         count = 0
#         for line in file:
#             grade = int(line.strip())
#             total += grade
#             count += 1

#         average = total / count
#         if average >= 90:
#             result = "A"
#         elif average >= 80:
#             result = "B"
#         elif average >= 70:
#             result = "C"
#         else:
#             result = "F"
#     print("The student's average grade is:", average)
#     print("The student's final grade is:", result)

#     a) Reads the student's grades from "grades.txt," calculates the 
#     average, and prints the average and the corresponding letter grade.

# 21. What does the following code snippet do?
#     with open("numbers.txt", "r") as file:
#         for line in file:
#             number = int(line.strip())
#             if number % 2 == 0:
#                 print(number, "is even.")
#             else:
#                 print(number, "is odd.")

#     a) Reads the numbers from "numbers.txt," checks if each number is even 
#     or odd, and prints the result for each number.

# 22. What will the following code snippet do?
#     with open("data.txt", "r") as file:
#         lines = file.readlines()
#         for line in lines:
#             if "important" in line:
#                 print(line)

#     a) Reads the entire file "data.txt" and prints lines containing 
#     the word "important."

# 23. What does the following code snippet do?
#     with open("students.txt", "r") as file:
#         for line in file:
#             if len(line.strip()) > 10:
#                 print("Long name:", line.strip())
#             else:
#                 print("Short name:", line.strip())

#     a) Reads the names of students from "students.txt" and prints "Long name:" 
#     for names with more than 10 characters and "Short name:" for names with 10 or fewer characters.

# 24. What is the default file mode used when opening a file in Python if you
# don't specify a mode explicitly using the 'r', 'w', 'a', or other mode flags?
#     a) 'r' (read mode)

