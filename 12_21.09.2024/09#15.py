import random
# - For Loops -
'''A. Write a Python program that uses a for loop to print 
all even numbers from 1 to 20, inclusive. Use the continue 
statement to skip odd numbers during the iteration.
'''
for i in range(1, 21):
    if i % 2 != 0:
        continue
    print(i)

'''B. Write a Python program that asks the user to input 10 numbers. 
Use a for loop to iterate through the numbers. Print the sum of 
all numbers entered by the user. Use the break statement to exit 
the loop early if the user inputs a negative number.
'''
# sum = 0
# for i in range(10):
#     number = int(input('Number: '))
#     if number < 0:
#         print(sum)
#         break
#     sum += number
# print(sum)

'''C. Write a Python program that takes an integer as input from 
the user and prints its multiplication table up to 10 using a for loop. 
Use the continue statement to skip the multiplication if the result 
is less than 30.
'''
# number = int(input('Number: '))
# for i in range(1, 11):
#     if i * number < 30:
#         continue
#     print(f'{number} x {i} = {i * number}')


'''D. Write a Python program to find and print all prime numbers between 
1 and 50 using a for loop. Use the break statement to exit the loop 
early if a non-prime number is encountered.
'''
print('prime numbers')

find_composite = False
for i in range(2, 51):
    # if i in [1, i]:
    #     continue
    j = 2
    while j < i:
        if i % j == 0:
            find_composite = True
            break
        j += 1
    
    if find_composite:
        print(f'{i} is non-prime')
        break
    else:
        print(f'{i} is prime')
        




'''E. Write a Python program to generate and print the first 10 numbers 
in the Fibonacci sequence using a for loop. Use the continue statement 
to skip printing a number if it is greater than 100.
'''

print('Fibonacci sequence')
fib = [ ]
for i in range(11):
    if i < 2:
        fib.append(i)
    else:
        if (fib[-2] + fib[-1]) > 100:
            continue
        fib.append(fib[-2] + fib[-1])
print(fib)
    

'''F. Write a Python program that asks the user to input an integer n. 
Using a for loop, print all even numbers in reverse order from n down 
to 2. Use the continue statement to skip odd numbers during the iteration.
'''
# print('even numbers')
# number = int(input('Number: '))
# for i in range(number, 0, -1):
#     if i % 2 != 0:
#         continue
#     print(i)

'''G. Write a Python program that prompts the user for a password. Use a for 
loop to iterate over a predefined list of passwords. If the entered password 
matches any of the predefined passwords, print "Access granted" and use the 
break statement to exit the loop. If no match is found, print "Access denied".
'''
# pasword_list = ['123', '321', 'qwerty', 'asdfg']
# password = input('Password: ')
# for pas in pasword_list:
#     if pas == password:
#         print('Access granted')
#         break
# else:
#     print('Access denied')
        


'''H. Write a Python program that asks the user to enter a series of numbers. 
Use a for loop to iterate through the numbers. Compute and print the average 
of all positive numbers entered by the user. Use the continue statement 
to skip negative numbers during the calculation.
'''
# print('average of all positive numbers')
# numbers = [ ]
# for _ in range(10):
#     number = int(input('Number: '))
#     if number < 0:
#         continue
#     numbers.append(number)
# avg = sum(numbers) / len(numbers)
# print(f'List: {numbers}\n average: {avg}')


'''I. Write a Python program that prompts the user to input a sentence. 
Use a for loop to iterate through the characters in the sentence and count 
the number of vowels (a, e, i, o, u). Print the total count of vowels. 
Use the continue statement to skip counting for non-alphabetic characters.
'''
# print('vowels')
# vowels = {
#     'a': 0,
#     'e': 0,
#     'i': 0,
#     'o': 0,
#     'u': 0
#     }
# sentence = input('Sentence: ')
# for x in sentence:
#     if not x.isalpha():
#         continue
#     if x in vowels.keys():
#         vowels[x] +=1
# print(vowels)
# print(f'Total vowels: {sum(list(vowels.values()))}')


'''J. Write a Python program that generates a random password of a specified 
length based on user input. Ask the user to input the desired password 
length and use a for loop to generate and print the password. Use the 
break statement to exit the loop after generating the password.
'''
# print('random password')
# length = int(input('Password length, max 64: '))
# password_chars = []
# chars = range(48, 123)
# for i in range(10):
#     selected_char = random.randrange(48, 122)
#     password_chars.append(chr(selected_char))
#     if i == length:
#         break
# password = ''.join(password_chars)
# print(f'Password is: {password}')


'''K. Write a Python program that prompts the user to enter the names of 
three cities and their corresponding populations. Use a for loop to populate 
a dictionary where the city names are keys and the populations are values.
'''
# print('cities and their populations')
# cities = {}
# length = [x for x in range(3)]
# for i in range(3):
#     city = input('City: ')
#     population = int(input('Population: '))
#     while cities.get(city):
#         print('city already has')
#         city = input('City: ')
#         population = int(input('Population: '))
#     cities.update({city: population})
# print(cities)


'''L. Write a Python program that asks the user to input a sentence. Use a for 
loop to iterate through the characters in the sentence and count the number 
of vowels (a, e, i, o, u). Store the counts in a dictionary where the vowels 
are keys and the counts are values.
'''
# print('vowels')
# vowels = {
#     'a': 0,
#     'e': 0,
#     'i': 0,
#     'o': 0,
#     'u': 0
#     }
# sentence = input('Sentence: ')
# for x in sentence:
#     if not x.isalpha():
#         continue
#     if x in vowels.keys():
#         vowels[x] +=1
# print(vowels)

'''M. Write a Python program that allows the user to enter key-value pairs into 
a dictionary. Prompt the user to input a key and a value, and use a for loop 
to allow them to enter multiple pairs. Print the dictionary after each addition.
'''
# print('key-value pairs into a dictionary')
# user_input = {}
# for i in range(5):
#     key = input('Key: ')
#     value = input('value: ')
#     user_input.update({key: value})
#     print(user_input)

'''N. Write a Python program that prompts the user to input a word or phrase. 
Use a for loop to iterate through the characters and count the frequency of 
each letter in the input. Store the counts in a dictionary where the letters 
are keys and the counts are values.
'''
# print('Store the counts in a dictionary')
# chars_dict = {}
# phrase = input('Phrase: ').strip()
# phrase = ''.join(phrase.split())
# for x in phrase:
#     chars_dict.update({x: chars_dict.get(x, 0) + 1})
# print(chars_dict)

'''O. Write a program to use for loop to print the following reverse number pattern:
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1
'''
numbers = [str(x) for x in range(5, 0, -1)]
print(numbers)
for i in numbers:
    numbers_str = ' '.join(numbers[numbers.index(i):])
    print(numbers_str)

'''P. Display numbers from -10 to -1 using for loop. The step of your range
method should be positive, not negative. The output:
-10
-9
-8
-7
-6
-5
-4
-3
-2
-1
'''
print('Display numbers from -10 to -1')
for x in range(-10, 0):
    print(x)

# - EXTRA HARD -
'''Task 1.
Count the total number of digits in a number.
Write a program to count the sum of digits in a number.
For example, the number is 75869, so the output should be 35 (7 + 5 + 8 + 6 + 9).
'''
print('Count the total number of digits')
number = input('Number: ') # Method 1
count = len(number)
print(f'Count: {count}')
digit_array = [int(x) for x in number]
total = sum(digit_array)
print(f'Number is {number}, sum of digits: {total}')

number = int(number)    # Method 2
total = 0
for x in range(len(str(number))):
    total += number % 10
    number = number// 10
print(f'Number is {number}, sum of digits: {total}')

'''Task 2.
Write a program to calculate the sum of series up to n term. 
For example, if n = 5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690
'''


# Task 3.
# Write a program to display whether the number is prime or not.
# Prime numbers are natural numbers that are divisible by only 1 and the number itself.

# - Chat GPT's Project -
# Project: Password Validation

# Write a Python program that prompts the user to enter a password. The program 
# should check the validity of the password based on the following conditions:

# The password must be at least 8 characters long.
# The password must contain at least one uppercase letter, one lowercase letter, 
# and one numeric digit.
# The password must not contain the word "password" (case insensitive).
# Use a for loop to iterate through the characters of the password and implement 
# the following actions:

# If the current character is a space, use continue to skip the rest of the loop 
# and move to the next character.
# If the password contains the word "password" (case insensitive), use break to 
# immediately exit the loop and print "Invalid password".
# After the loop, check if the password meets all the conditions. If it does, 
# print "Valid password". Otherwise, print "Invalid password".
# Ensure that the program provides appropriate messages to guide the user and 
# thoroughly tests the input for validity.

# This task challenges the usage of for loops, break, and continue to handle 
# complex conditions and ensure secure password validation. Happy coding!

# Quiz.
# 1. What is the purpose of the continue statement in a for loop?
#     a) It terminates the loop and exits the loop block.
#     b) It skips the rest of the loop and moves to the next iteration.
#     c) It restarts the loop from the beginning.
#     d) It checks if the loop condition is met.

# 2. In a for loop, the break statement is used to:
#     a) Skip the current iteration and proceed to the next.
#     b) Exit the loop and move to the next block of code.
#     c) Restart the loop from the beginning.
#     d) None of the above.

# 3. Which of the following statements is true about the for loop in Python?
#     a) The loop variable can only be a numeric data type.
#     b) The loop variable can be of any data type.
#     c) The loop variable is optional.
#     d) The loop variable is not required in a for loop.

# 4. For the following code snippet, determine the output or the result of the operation:
#     numbers = [1, 2, 3, 4, 5]
#     total = 0
#     for num in numbers:
#         if num % 2 == 0:
#             total += num
#         else:
#             continue
#     print(total)

# 5. For the following code snippet, determine the output or the result of the operation:
#     numbers = [10, 20, 30, 40, 50]
#     total = 0
#     for num in numbers:
#         if num > 30:
#             break
#         if num % 2 == 0:
#             total += num
#         else:
#             continue
#     print(total)

# 6. What is the value of the var after the for loop completes its execution:
#     var = 10
#     for i in range(10):
#         for j in range(2, 10, 1):
#             if var % 2 == 0:
#                 continue
#                 var += 1
#         var += 1
#     else:
#         var += 1
#     print(var)

#     a) 20
#     b) 21
#     c) 10
#     d) 30

# 7. What is the output of the following range() function:
#     for num in range(2,-5,-1):
#         print(num, end=", ")

#     a) 2, 1, 0
#     b) 2, 1, 0, -1, -2, -3, -4, -5
#     c) 2, 1, 0, -1, -2, -3, -4

# 8. What is the value of x after the following nested for loop completes its execution:
#     x = 0
#     for i in range(10):
#         for j in range(-1, -10, -1):
#             x += 1
#             print(x)
    
#     a) 99
#     b) 90
#     c) 100

# 9. What is the output of the following nested loop?
#     for num in range(10, 14):
#         for i in range(2, num):
#             if num % i == 1:
#                 print(num)
#                 break
                
# 10. What is the output of the following nested loop?
#     numbers = [10, 20]
#     items = ["Chair", "Table"]

#     for x in numbers:
#         for y in items:
#             print(x, y)
        
#     a)
#     10 Chair
#     10 Table
#     20 Chair
#     20 Table
#     b)
#     10 Chair
#     10 Table

# 11. What is the output of the following loop?
#     for l in 'Jhon':
#         if l == 'o':
#             pass
#         print(l, end=", ")
            
#     a) J, h, n,
#     b) J, h, o, n,

# - True or False -
# True or False: A for loop in Python can be nested within another for loop.
# True or False: The continue statement is used to immediately exit the loop
# and terminate the program.
# True or False: The break statement is used to exit the loop prematurely, 
# regardless of whether the loop condition is met.
# True or False: The break statement is used to skip the rest of the loop and 
# move to the next iteration.
# True or False: The continue statement is used to exit the loop prematurely, 
# regardless of whether the loop condition is met.
# True or False: Using break is more appropriate when you want to exit the 
# loop prematurely based on a certain condition, regardless of whether the 
# loop has completed all iterations. It allows you to terminate the loop early 
# and continue with the rest of the program.
# True or False: Using continue is more appropriate when you want to skip the 
# current iteration and proceed to the next iteration based on a certain condition, 
# but you still want to continue the loop.
# """