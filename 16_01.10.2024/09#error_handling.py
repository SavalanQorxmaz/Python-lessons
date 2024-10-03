

# Instructions. Write Python programs to solve the following tasks,focusing 
# on error handling using try and except blocks. In each program, you should 
# handle potential errors gracefully and provide appropriate error messages.

# - Error Handling -
'''A. Divide by Zero:
Write a program that takes two numbers as input from the user and 
calculates their division result. Handle the ZeroDivisionError exception 
that might occur if the user attempts to divide by zero. Display an error 
message in such cases.
'''
print('Divide by Zero')
correct = [False, False]
while not all(correct) :
    if not correct[0]:
        try:
            bolunen = input('Bolunen: ')
            bolunen = int(bolunen)
            correct[0] = True
        except ValueError:
            print('yanlis format')
            pass
    if not correct[1]:
        try:
            bolen = input('Bolen: ')
            bolen = int(bolen)
            correct[1] = True
        except ValueError:
            print('yanlis format')
            pass
try:
    result = bolunen / bolen
    print(f'Qismet: {result}') 
except ZeroDivisionError:
    print('Sifira bolme olmaz')  

'''B. File Reading:
Write a program that reads the content of a file specified by the 
user. Handle the FileNotFoundError exception if the file does not exist, 
and display an error message. If the file exists, display its content.
'''
print('File Reading')
try:
    file = open('Files/b.txt', 'r')
    print(file.read())
except FileNotFoundError:
    file = open('Files/b.txt', 'w')
    file.write('First line')
    file.close()
finally:
    file = open('Files/b.txt', 'r')
    print(file.read())
    file.close() 
    

'''C. List Element Access:
Create a list with some elements, and then write a program that asks the 
user for an index to access an element from the list. Handle the IndexError 
exception if the user provides an index that is out of bounds and display an error message.
'''
print('List Element Access')
lst = [1, 2, 3, 4, 5, 6, 7]
try:
    print(lst[100])
except IndexError:
    print('Index out of range')


'''D. Dictionary Key Access:
Create a dictionary with some key-value pairs. Write a program that prompts the
user for a key and attempts to access the corresponding value. Handle the 
KeyError exception if the user enters a key that does not exist in the 
dictionary and display an error message.
'''
print('Dictionary Key Access')
my_dict = {
    'name': 'Bob',
    'age': 25,
    'city': 'Baku',
}
try:
    school = my_dict['school']
except KeyError:
    print(f'Key not found')


'''E. Word Counter:
Write a program that reads the content of a text file specified by the user 
and counts the number of words in it. Handle the FileNotFoundError exception if the 
file does not exist and display an error message.
'''
print('Word Counter')
have_text = False
while not have_text:
    text = input('Write text: ')
    if len(text) > 0:
        file = open('user_file.txt', 'a')
        file.write(text)
        file.close()
        try:
            file = open('user_file.txt', 'r')
            print(file.read())
        except FileNotFoundError:
            print('File not found')
        else:
            file.close()
            have_text = True
            
        
        



'''F. Module Import:
Write a program that tries to import 'django' module. Handle the occuring exception 
if the module does not exist and display an error message.
'''
print('Module Import')
try:
    import django
    print(django.get_version())
except ModuleNotFoundError:
    print('Module not found')

'''G. User Input:
Write a program that uses infinite loop and prompts the user until he/she inputs an integer.
When the input is given properly, the loop should be exited and the program should print 'Exiting'.
'''
print('User Input')
number = None
try:
    number = int(input('Write number: ').strip())
except ValueError:
    correct = False
    while not correct:
        user_input = input('Write Integer number: ').strip()
        if user_input.isdigit():
           number = int(user_input)
           correct = True
finally:
    print(number)
    print('Exiting')
           


# Quiz.
# 1. What is error handling in programming?
#     c) A mechanism to gracefully deal with unexpected issues and exceptions
#     d) A method to prevent all types of errors in code

# 2. Which Python keyword is used to catch exceptions in a try-except block?
#     c) except
    
# 3. What will the following Python code snippet output?
#     try:
#         num = 10 / 0
#     except ZeroDivisionError:
#         print("Division by zero is not allowed.")

#     a) Division by zero is not allowed.

# 4. What is the purpose of the finally block in a try-except-finally structure?
#     c) It always executes, regardless of whether an exception is raised or not.

# 5. In Python, which of the following statements is true about exceptions?
#     c) Multiple except blocks can be used to catch different exceptions.

# 6. What is the primary purpose of raising a custom exception in Python?
#     c) To provide meaningful information about a specific error condition.

# 7. Which of the following statements is true about the else block in a try-except-else structure?
#     b) It executes only if no exception is raised.

# 8. What is the output of the following Python code snippet?
#     try:
#         x = int("abc")
#     except ValueError as e:
#         print(e)

#     c) invalid literal for int() with base 10: 'abc'

# 9. Which error handling approach allows you to specify different code blocks for different exceptions?
#     a) try-except

# 10. When using the with statement to open a file, what does it ensure regarding the file's state?
#     a) It guarantees that the file will be closed when the block is exited, even if an exception occurs.

# 11. Which of the following is NOT a built-in exception in Python?
#     b) CustomException

# 12. What is the output of the following Python code snippet?
#     try:
#         x = 5 / 0
#     except ZeroDivisionError as e:
#         print(e)
#     except Exception as e:
#         print("An error occurred:", e)
#     finally:
#         print("Finally block executed.")

#     a) "An error occurred: division by zero" followed by "Finally block executed."
    
# 13. In Python, what does the except keyword allow you to do when handling exceptions?
#     a) Specify the type of exception to catch
# 14. What type of error occurs when a variable is used before it has been assigned a value?
#     c) NameError

# 15. In a try-except block, can you have multiple except blocks for the same exception type?
#     b) No, you can have only one except block per exception type.

# 16. What is the purpose of the else block in a try-except-else structure?
#     d) It specifies code to execute if no exception is raised.