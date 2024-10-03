"""
Instructions. Write Python programs to solve the following tasks,focusing 
on error handling using try and except blocks. In each program, you should 
handle potential errors gracefully and provide appropriate error messages.

- Error Handling -
A. Divide by Zero:
Write a program that takes two numbers as input from the user and 
calculates their division result. Handle the ZeroDivisionError exception 
that might occur if the user attempts to divide by zero. Display an error 
message in such cases.

B. File Reading:
Write a program that reads the content of a file specified by the 
user. Handle the FileNotFoundError exception if the file does not exist, 
and display an error message. If the file exists, display its content.

C. List Element Access:
Create a list with some elements, and then write a program that asks the 
user for an index to access an element from the list. Handle the IndexError 
exception if the user provides an index that is out of bounds and display an error message.

D. Dictionary Key Access:
Create a dictionary with some key-value pairs. Write a program that prompts the
user for a key and attempts to access the corresponding value. Handle the 
KeyError exception if the user enters a key that does not exist in the 
dictionary and display an error message.

E. Word Counter:
Write a program that reads the content of a text file specified by the user 
and counts the number of words in it. Handle the FileNotFoundError exception if the 
file does not exist and display an error message.

F. Module Import:
Write a program that tries to import 'django' module. Handle the occuring exception 
if the module does not exist and display an error message.

G. User Input:
Write a program that uses infinite loop and prompts the user until he/she inputs an integer.
When the input is given properly, the loop should be exited and the program should print 'Exiting'.

Quiz.
1. What is error handling in programming?
    a) A technique to make code run faster
    b) A way to avoid writing error messages
    c) A mechanism to gracefully deal with unexpected issues and exceptions
    d) A method to prevent all types of errors in code

2. Which Python keyword is used to catch exceptions in a try-except block?
    a) try
    b) catch
    c) except
    d) catchexcept
    
3. What will the following Python code snippet output?
    try:
        num = 10 / 0
    except ZeroDivisionError:
        print("Division by zero is not allowed.")

    a) Division by zero is not allowed.
    b) 0
    c) 10
    d) An error message saying "ZeroDivisionError: division by zero"

4. What is the purpose of the finally block in a try-except-finally structure?
    a) It specifies the exception to be caught.
    b) It handles errors gracefully.
    c) It always executes, regardless of whether an exception is raised or not.
    d) It terminates the program if an exception occurs.

5. In Python, which of the following statements is true about exceptions?
    a) All exceptions are of the same type.
    b) Exceptions cannot be raised by user-defined functions.
    c) Multiple except blocks can be used to catch different exceptions.
    d) try-except blocks can be nested indefinitely.

6. What is the primary purpose of raising a custom exception in Python?
    a) To terminate the program immediately.
    b) To catch built-in exceptions more effectively.
    c) To provide meaningful information about a specific error condition.
    d) To ignore errors and continue program execution.

7. Which of the following statements is true about the else block in a try-except-else structure?
    a) It always executes, even if an exception is raised.
    b) It executes only if no exception is raised.
    c) It specifies the exception to be caught.
    d) It handles errors gracefully.

8. What is the output of the following Python code snippet?
    try:
        x = int("abc")
    except ValueError as e:
        print(e)

    a) "abc"
    b) 0
    c) invalid literal for int() with base 10: 'abc'
    d) No output; it raises an error and terminates the program.

9. Which error handling approach allows you to specify different code blocks for different exceptions?
    a) try-except
    b) try-finally
    c) try-else
    d) try-except-else

10. When using the with statement to open a file, what does it ensure regarding the file's state?
    a) It guarantees that the file will be closed when the block is exited, even if an exception occurs.
    b) It automatically handles all exceptions that may occur during file operations.
    c) It ensures that the file is locked for exclusive access during the block execution.
    d) It prevents the file from being modified during the block execution.

11. Which of the following is NOT a built-in exception in Python?
    a) ValueError
    b) CustomException
    c) TypeError
    d) ZeroDivisionError

12. What is the output of the following Python code snippet?
    try:
        x = 5 / 0
    except ZeroDivisionError as e:
        print(e)
    except Exception as e:
        print("An error occurred:", e)
    finally:
        print("Finally block executed.")

    a) "An error occurred: division by zero" followed by "Finally block executed."
    b) "division by zero" followed by "Finally block executed."
    c) "An error occurred: division by zero"
    d) "Finally block executed."
    
13. In Python, what does the except keyword allow you to do when handling exceptions?
    a) Specify the type of exception to catch
    b) Define the code to execute when no exception occurs
    c) Specify multiple types of exceptions to catch in a single block
    d) Terminate the program immediately

14. What type of error occurs when a variable is used before it has been assigned a value?
    a) Syntax error
    b) Runtime error
    c) NameError
    d) Semantic error

15. In a try-except block, can you have multiple except blocks for the same exception type?
    a) Yes, you can have multiple except blocks for the same exception type.
    b) No, you can have only one except block per exception type.
    c) It depends on the Python version being used.
    d) You cannot have except blocks for the same exception type.

16. What is the purpose of the else block in a try-except-else structure?
    a) It always executes, even if an exception is raised.
    b) It executes only if an exception is raised.
    c) It specifies the exception to be caught.
    d) It specifies code to execute if no exception is raised.
"""