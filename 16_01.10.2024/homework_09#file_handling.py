"""
Note. Use the with keyword to open and close the file, ensuring proper file handling.

- Working with Files -
A. Write a program to read an entire text file. The name of a file should 
be given by a user.
B. Write a program to read first n lines of a file.
C. Write a program to read last n lines of a file.
D. Write a program to read a file line by line and store it into a list.
E. Write a program to read a file line by line store it into a variable.
F. Write a python program to find the longest words.
G. Write a Python program to count the number of lines in a text file.
H. Write a Python program to count the frequency of words in a file.
I. Write a Python program to write a list to a file.
J. Write a Python program to combine each line from first file with the corresponding line in second file.
K. Write a program that combines two different file contents with titles ("File No.1", "File No.2")
before the content of each file
L. Write a Python program to read a random line from a file.
M. Write a Python program to assess if a file is closed or not.
N. Write a Python program to create a file where all letters of English alphabet are listed 
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
O. Suppose you have the following list:
filenames = [
    "bill.pdf",
    "invoice.pdf",
    "registration.pdf",
    "certificate.pdf"
]
Write a program that creates all those files.

- Chat GPT's Homework -
Task 1. Create a text file named "students.txt" with the names of five students, 
one name per line.
Task 2. Write a Python program that reads the contents of the "students.txt" file 
using the 'r' mode and prints each student's name on a separate line.
Task 3. Add a function to your program that allows the user to input the name of a
new student. Append this name to the "students.txt" file using the 'a' mode. 
Ensure that the name is written on a new line.
Task 4. Implement a feature that lets the user update a student's name. Ask the 
user to input the old name of the student they want to update and the new name. 
Update the "students.txt" file accordingly. Make sure to handle cases where 
the student's name may appear more than once.
Task 5. After each operation (reading, adding, updating), display the updated 
list of students to the user.
Task 6. Allow the user to search for a student's name in the list and display 
whether or not the student is present in the file.

Quiz.
1. What is the primary purpose of using the with statement (with context 
manager) when working with files in Python?
    a) To read the contents of a file.
    b) To write data to a file.
    c) To ensure proper file handling by automatically opening and closing the file.
    d) To check if a file exists in the system.

2. What are the benefits of using the with statement for file handling in Python?
    a) It makes the code shorter.
    b) It improves error handling.
    c) It automatically opens and closes the file.
    d) It prevents file corruption.

3. What can happen if you don't close files before exiting a Python program?
    a) It can lead to a memory leak.
    b) It can result in a syntax error.
    c) It may cause data corruption or loss.
    d) It has no impact on the program.

4. Why is it important to close files after you're done with them in a Python program?
    a) To free up system resources.
    b) To speed up file access.
    c) To make the code more readable.
    d) To ensure that the file is read-only.

5. Which file mode is used for reading a file in Python?
    a) 'r'
    b) 'w'
    c) 'a'
    d) 'x'

6. What keyword is used to ensure proper file handling, automatically 
closing the file when done?
    a) close()
    b) exit()
    c) with
    d) end

7. What mode should you use to open a file for writing, and create a new 
file if it doesn't exist, or truncate the file if it exists?
    a) 'r'
    b) 'a'
    c) 'w'
    d) 'x'

8. How can you read the entire content of a file and store it as a string in Python?
    a) Using the readline() method
    b) Using the readlines() method
    c) Using the read() method
    d) Using the write() method

9. What file mode should you use to add new data to an existing file 
without overwriting its content?
    a) 'r'
    b) 'a'
    c) 'w'
    d) 'x'

10. Which of the following Python code snippets correctly opens a file 
in read mode, reads its contents line by line, and prints them?
    a)
    file = open("data.txt", "r")
    for line in file:
        print(line)
    b)
    file = open("data.txt", "r")
    contents = file.read()
    print(contents)
    c)
    file = open("data.txt", "r")
    lines = file.readlines()
    for line in lines:
        print(line)
    d)
    file = open("data.txt", "r")
    print(file)

11. How can you add a new line of text to an existing file in Python 
without overwriting its existing content?
    a) Open the file in 'r' mode and write the new line of text.
    b) Open the file in 'w' mode and write the new line of text.
    c) Open the file in 'a' mode and write the new line of text.
    d) Use the append() method to add the new line of text.

12. To update a specific piece of data within an existing file, you should:
    a) Open the file in 'w' mode and write the updated data.
    b) Open the file in 'a' mode and append the updated data.
    c) Read the entire file, modify the data in memory, and rewrite the entire file.
    d) Use the update() method to modify the data within the file.

13. Which of the following is a good practice when working with files in Python?
    a) Leaving files open to save time on opening and closing.
    b) Using the try...except statement without handling file exceptions.
    c) Closing files explicitly using the close() method.
    d) Storing all file data in a single string for easy manipulation.

14. What does the 'x' mode do when opening a file?
    a) Opens the file for reading.
    b) Opens the file for writing and creates a new file if it doesn't exist.
    c) Opens the file for appending.
    d) Opens the file for exclusive access, but creates a new file if it doesn't exist.

15. What does the following code snippet do?
    with open("file.txt", "w") as file:
        file.write("Hello, World!")

    a) Opens the file "file.txt" for reading and prints "Hello, World!" to the console.
    b) Opens the file "file.txt" for writing and overwrites its content with "Hello, World!".
    c) Appends "Hello, World!" to the end of the file "file.txt".
    d) Raises an error because you can't write to a file using a with block.

16. If you want to read the first 100 characters from a file named "data.txt" 
and store them in a variable, which code snippet should you use?
    a)
    with open("data.txt", "r") as file:
        data = file.read(100)
    b)
    with open("data.txt", "r") as file:
        data = file.read()
        data = data[:100]
    c)
    with open("data.txt", "r") as file:
        data = file.read(100)
        file.close()
    d)
    with open("data.txt", "r") as file:
        data = file.readline(100)

17. What will the following code snippet do?
    with open("file.txt", "a") as file:
        file.write("Line 1\nLine 2\nLine 3")

    a) Appends the text "Line 1\nLine 2\nLine 3" as a single line to the end of the file.
    b) Appends three lines to the end of the file: "Line 1", "Line 2", and "Line 3".
    c) Appends the text "Line 1\nLine 2\nLine 3" as separate lines to the end of the file.
    d) Raises an error because you can't append multiple lines at once using the 'a' mode.

18. What is the purpose of the 'b' mode when opening a file in Python?
    a) Opens the file for binary read/write operations.
    b) Opens the file for reading in binary mode, allowing non-text files to be read.
    c) Opens the file for writing in binary mode, allowing non-text data to be written.
    d) Encrypts the file for security purposes.

19. What does the following code snippet do?
    with open("data.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            print(line.strip())

    a) Reads the entire file "data.txt" and prints its contents.
    b) Reads the first line of the file "data.txt" and prints it.
    c) Reads all lines from the file "data.txt" and prints them without trailing newline characters.
    d) Raises an error because you can't use readlines() in a with block.

20. What does the following code snippet do?
    with open("grades.txt", "r") as file:
        total = 0
        count = 0
        for line in file:
            grade = int(line.strip())
            total += grade
            count += 1

        average = total / count
        if average >= 90:
            result = "A"
        elif average >= 80:
            result = "B"
        elif average >= 70:
            result = "C"
        else:
            result = "F"
    print("The student's average grade is:", average)
    print("The student's final grade is:", result)

    a) Reads the student's grades from "grades.txt," calculates the 
    average, and prints the average and the corresponding letter grade.
    b) Reads the student's grades from "grades.txt," prints each grade 
    individually, and calculates the total number of grades.
    c) Raises an error because you can't use strip() with a file object.
    d) Reads the student's grades from "grades.txt," calculates the average, 
    but doesn't print any results.

21. What does the following code snippet do?
    with open("numbers.txt", "r") as file:
        for line in file:
            number = int(line.strip())
            if number % 2 == 0:
                print(number, "is even.")
            else:
                print(number, "is odd.")

    a) Reads the numbers from "numbers.txt," checks if each number is even 
    or odd, and prints the result for each number.
    b) Reads the numbers from "numbers.txt," calculates the sum of all even 
    numbers, and prints the result.
    c) Raises an error because you can't use the modulus operator (%) with a file object.
    d) Reads the numbers from "numbers.txt," prints them without checking if 
    they are even or odd.

22. What will the following code snippet do?
    with open("data.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            if "important" in line:
                print(line)

    a) Reads the entire file "data.txt" and prints lines containing 
    the word "important."
    b) Reads the entire file "data.txt" and prints the lines that don't 
    contain the word "important."
    c) Raises an error because you can't use the in keyword with a file object.
    d) Reads the first line of the file "data.txt" and prints it.

23. What does the following code snippet do?
    with open("students.txt", "r") as file:
        for line in file:
            if len(line.strip()) > 10:
                print("Long name:", line.strip())
            else:
                print("Short name:", line.strip())

    a) Reads the names of students from "students.txt" and prints "Long name:" 
    for names with more than 10 characters and "Short name:" for names with 10 or fewer characters.
    b) Reads the names of students from "students.txt" and prints "Long name:" 
    for names with 10 or fewer characters and "Short name:" for names with more than 10 characters.
    c) Raises an error because you can't use len() with a file object.
    d) Reads the entire file "students.txt" and prints all the names without any distinction.

24. What is the default file mode used when opening a file in Python if you
don't specify a mode explicitly using the 'r', 'w', 'a', or other mode flags?
    a) 'r' (read mode)
    b) 'w' (write mode)
    c) 'a' (append mode)
    d) 'x' (exclusive creation mode)
"""