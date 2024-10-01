from random import randint, choice
import string

# - For Loops -
print('''A. Write a program to use the loop to find the factorial of a given number.
''')
number = None
correct = False
while not correct:
    user_input = input("Enter number: ").strip()
    try: 
        number = int(user_input) 
        correct = True 
    except:
        print(f'Incorrect format: {user_input}')
fact = 1
step = number
while step > 0:
    fact *= step
    step -= 1
print(f'{number}! = {fact}')

print('''B. Write a program that uses a for loop to print numbers from 1 to 10. However, 
if the number is divisible by 3, skip the loop, and if the number is 7, stop the loop.
''')
for i in range(1, 10):
    if i % 3 == 0:
        continue
    elif i == 7:
        break
    else:
        print(i)

'''C. In Python, what is the purpose of the range() function when used with a for loop?
'''
# for i in range(Number) --> i =1,2,..,9

'''D. How can you prematurely exit a for loop in Python?
'''
# break

'''E. What is an iterator in Python, and how is it related to for loops?
'''
# iterators --> if they have enter() and next() methods
lst = [1, 2, 3]
for x in lst:
    pass

'''F. How can you iterate through the elements of a list in reverse order using a for loop?
'''
lst = [1, 2, 3, 4]
reversed_lst = [ ]
for x in lst:
    reversed_lst.insert(0, x)

print('''G. Create a for loop that prints all even numbers from 20 to 40. Solve this task in
two different ways (modifying range() and using if-statements).
''')
print('Method 1')
for x in range(20, 41, 2):
    print(x)
print('Method 2')
for i in range(20, 41):
    if i % 2 == 0:
        print(i)
print('Method 3')
for i in range(20, 41):
    if i % 2 != 0:
        continue
    print(i)

print('''H. Write a for loop to calculate the sum of all integers from 1 to 100. At the end of the loop 
the program should print 'The end of a task.'
''')
total = 0
for i in range(1, 101):
    total += i
    print(f'Total {i}: {total}')
else:
    print('The end of a task.')

print('''I. Generate a multiplication table for a given number using a for loop, e.g., for the number 5, print 5x1, 5x2, ..., 5x10.
''')
number = None
correct = False
while not correct:
    user_input = input("Enter number: ").strip()
    try: 
        number = int(user_input)    
        correct = True
    except:
        print(f'Incorrect format: {user_input}')
for i in range(number):
    print(f'{number} x {i} = {number * i}')

print('''J. Write a for loop to iterate through a string and print each character on a separate line
with corresponding index.
''')
word = 'I learn Python'
for x in word:
    print(x)

print('''K. Suppose you have the following list:
employees = ["Bob", "John", "Brad", "Jake", "Michael", "Jim"]

Iterate over this list and print all names except the ones which start with the
letter 'J'.
''')
employees = ["Bob", "John", "Brad", "Jake", "Michael", "Jim"]
for employee in employees:
    if employee.startswith('J'):
        continue
    print(employee)

print('''L. Suppose you have the following list:
stock = ["Cherry", "Lemon", "Watermelon", "Carrot", "Banana", "Coconut", "Pumpkin", "Apple", "Grape", "Cucumber"]

Iterate over this list and print all fruits and vegetables except the ones which start with the
letter 'C' and whichs length is less than or equal 6.
''')
stock = ["Cherry", "Lemon", "Watermelon", "Carrot", "Banana", "Coconut", "Pumpkin", "Apple", "Grape", "Cucumber"]
for fruit in stock:
    if fruit.startswith('C') or len(fruit) < 7:
        continue
    print(fruit)

print('''M. Write a for loop to reverse a given string. For example, "hello" should become 'olleh'.
You shouldn't use any reversing methods such as [::-1]. Instead you should make manipulations
with string literals.
''')
word = 'Python'
lst = [ ]
for x in word:
    lst.insert(0, x)
print(f'word: {word}, reversed word: {''.join(lst)}')

print('''N. Write a for loop to check and print all prime numbers within a given range (on dynamic user input).
''')
number = None
correct = False
while not correct:
    user_input = input("Enter number: ").strip()
    try: 
        number = int(user_input)    
        correct = True
    except:
        print(f'Incorrect format: {user_input}')
for i in range(2, number+1):
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print(i)


'''O. Implement a for loop to search for a specific word in a text and replace it with another word.
'''
sentence = 'i learn javascript'
word = 'python'
replaced_sentence = None
find = 'javascript'
length = len(sentence)
for i in range(length):
    if sentence.startswith(find, i):
        replaced_sentence = sentence.replace(find, word)
        break
print(replaced_sentence)
    
'''P. Write a program that draws the pyramid as:
Reverse Pyramid
  ***********     
   *********
    *******
     *****
      ***
       *
'''
print('Reversed Pyramid')
for i in range(11, 0, -2):
    print(f'{('*' * i).center(20)}')

'''Q. Write the shortest program that prints the position and each character of a string.
'''
word = 'Python'
for i, char in enumerate(word):
    print(f'{i+1}: {char}')

'''R. You have the following dictionary:
data = {
    "key1": 80,
    "key2": 75,
    "key3": 65,
    "key4": 85
}
Iterate over it and check if any value is less than 80, add the missing points.
'''
data = {
    "key1": 80,
    "key2": 75,
    "key3": 65,
    "key4": 85
}
for x in data:
    if data[x] < 80:
        print(f'{x}: {data[x]}')


'''S. Copy this code to your file:
from random import randint
numbers = [randint(15, 40) for _ in range(5)]

This gives you a list of 5 random numbers between 15 and 40. Using for loops
find the max value of that list, and print the list to see values.
'''
numbers = [randint(15, 40) for _ in range(5)]
max_value = numbers[0]
for x in numbers:
    if x > max_value:
        max_value = x
print(numbers)
print(f'Max value: {max_value}')

'''T. Use 'numbers' list from Task S. Iterate over it again, and if there is a number
between 20 and 25 exit the loop, otherwise print the value.
'''
numbers = [randint(15, 40) for _ in range(5)]
print(numbers)
for x in numbers:
    if 20 <= x <= 25:
        break
    print(x)

'''U. Write a Python program to construct the following pattern:
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
'''
step = 1
to_right = True
while step != 0:
    print('* ' * step)
    if to_right:
        step += 1
    else:
        step -= 1
    if step == 5:
        to_right = False
    

'''V. Write a Python program to count the number of even and odd numbers in a collection of numbers.
'''
numbers = [1, 28, 37, 23, 47, 36, 124, 238, 8]
odds = 0
evens = 0
for x in numbers:
    if x % 2 == 0:
        evens +=1
    else:
        odds += 1
print(numbers)
print(f'evens: {evens}\nodds: {odds}')

'''W. Write a Python program that prints each item and its corresponding type from the following list.
[5, True, "Python", (1, 2, 3), [5, 6, 7], 9.99, {"name":"Mark"}]
'''
lst = [5, True, "Python", (1, 2, 3), [5, 6, 7], 9.99, {"name":"Mark"}]
for x in lst:
    print(f'{x} is {type(x)} type')

'''X. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
'''
for i in range(7):
    if i == 3 or i == 6:
        continue
    print(i)

'''Y. Write a Python program that accepts a string and calculates the number of digits and letters.
'''
sentence = 'There are 5 apples and 3 pears'
digits = 0
letters = 0
for x in sentence:
    if x.isdigit():
        digits += 1
    elif x.isalpha():
        letters += 1
print(f'Sentence: {sentence}\nDigits: {digits}\nLetters: {letters}')

print('''Z. Write a Python program to guess a number between 1 and 9. The program should use 'random' module,
give only 3 chances to guess the number. Print 'Congratulations' if you guess and 'Game Over'
if you fail.
''')
random_number = randint(1, 9)
number = None
for i in range(3):
    correct = False
    while not correct:
        user_input = input("Enter number: ").strip()
        try: 
            number = int(user_input) 
            if 1 <=number <= 9:
                print(f'Your number is: {number}')
                correct = True
            else:
                print(f'wrong diapason {number}')
        except:
            print(f'Incorrect format: {user_input}')
    if random_number == number:
        print('Congratulations')
    elif i == 2:
        
        print(f'Game over, System number: {random_number}')
    else:
        print(f'You have {2 - i} chance')


# - Chat GPT's Homework -

print('''Problem 1: Generate a Series
Write a Python program that uses a for loop to generate and print the following 
series of numbers: 1, 4, 9, 16, 25, ... up to a given positive integer n. The 
series consists of perfect squares.
''')
number = None
correct = False
while not correct:
    user_input = input("Enter number: ").strip()
    try: 
        number = int(user_input) 
        if number > 0:
            print(f'Your number is: {number}')
            correct = True
        else:
                print(f'Only positibe number')
    except:
        print(f'Incorrect format: {user_input}')
for i in range(number+1):
    print(i**2)

'''Problem 2: Calculate Factorial with a For Loop
Write a Python program that calculates the factorial of a given positive integer n 
using a for loop. Display the result.
'''
print('Calculate Factorial with a For Loop')
number = None
correct = False
while not correct:
    user_input = input("Enter number: ").strip()
    try: 
        number = int(user_input) 
        if number > 0:
            print(f'Your number is: {number}')
            correct = True
        else:
                print(f'Only positibe number')
    except:
        print(f'Incorrect format: {user_input}')
fact = 1
for i in range(number, 1, -1):
    fact *= i
print(fact)

'''Problem 3: Password Generator
Write a Python program that generates a random password consisting of both uppercase 
and lowercase letters, digits, and special characters. The password should be of a 
specified length n. Use a for loop to create the password.
'''
print('Password Generator')
strs = string.printable
password = [ ]
lwrs = strs.find('a')
uprs = strs.find('A')
spcs = strs.find('!')

digits = [ ]
uppers = [ ]
lowers = [ ]
specs = [ ]
for i in range(len(strs)-10):
    if i < lwrs:
        digits.append(strs[i])
    elif i < uprs:
        lowers.append(strs[i])
    elif i < spcs:
        uppers.append(strs[i])
    else:
        specs.append(strs[i])
length = 8
dgt_count = randint(1, length-3)
length -= dgt_count
lwr_count = randint(1, length-2)
length -= lwr_count
upr_count = randint(1, length-1)
length -= upr_count
spc_count = length
count_dict = {
    'digits': [dgt_count, digits],
    'lowers': [lwr_count, lowers],
    'uppers': [upr_count, uppers],
    'specs': [spc_count, specs]
}
# print(choice(list(count_dict.keys())))
for i in range(8):
    char_type = choice(list(count_dict.keys()))
    # print(char_type)
    char = choice(count_dict[char_type][1])
    # print(char)
    password.append(char)
    count_dict[char_type][0] -= 1 
    if count_dict[char_type][0] == 0:
        del count_dict[char_type]
# print(count_dict)
print(f'Password: {''.join(password)}')


'''Problem 4: Average of Numbers
Write a Python program that calculates the average of a list of numbers using a 
for loop. Prompt the user to enter a list of numbers (comma-separated), and then 
compute and display the average.
'''
print('Average of Numbers')
str_list = input('enter a list of numbers (comma-separated): ')
print(str_list)
lst = str_list.split()
print(lst)
numbers = [ ]
for x in lst:
    if x.isdigit():
        numbers.append(int(x))
total = 0
length = len(numbers)
for x in numbers:
    total += x
average = total / length
print(f'Numbers list: {numbers}\nAverage: {average}')

'''Problem 5: Pattern Printing
Write a Python program that prints the following pattern using nested for loops:
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''
print('Problem 5: Pattern Printing')
lst = []
for i in range(1, 6):
    lst.append(str(i))
    print(' '.join(lst))


'''Problem 6: Count Vowels and Consonants
Write a Python program that counts the number of vowels and consonants in a given 
string. Use a for loop to iterate through the characters of the string and 
categorize them as vowels or consonants. Display the counts separately.
'''
print('Problem 6: Count Vowels and Consonants')
vowels = ''.join(['a', 'i', 'o', 'u', 'e'])
print(f'Vowels: {vowels} ')
sentence = input('Sentence or word: ').strip().lower()
vowel_count = 0
constant_count = 0
for x in sentence:
    if  not x.isalpha():
        continue
    else:
        if x in vowels:
            vowel_count += 1
        else:
            constant_count += 1
print(f'Vowels: {vowel_count}\nConstants: {constant_count}')

'''Problem 7: Reverse a List
Write a Python program that takes a list as input and uses a for loop to reverse 
the order of elements in the list. Display the reversed list.
'''
print('Problem 7: Reverse a List')
user_input = input('enter a list (comma-separated): ')
lst = user_input.split()
print(f'List: {lst}')
length = len(lst)
for i in range(length // 2):
    temp = lst[i]
    lst[i] = lst[length-1-i]
    lst[length-1-i] = temp
print(f'reversed list: {lst}')


'''Problem 8: Finding Factors
Write a Python program that prompts the user to enter a positive integer and 
then finds and prints all the factors of that integer using a for loop.
'''
print('Problem 8: Finding Factors')
correct = False
number = None
factor_list = [ ]
while not correct:
    user_input = input('Positive number: ')
    if user_input.isdigit():
        number = int(user_input)  
        correct = True
        break
    else:
        print('Only Positive number')
for i in range(1, number+1):
    if number % i == 0:
        factor_list.append(i)
print(factor_list)
length = len(factor_list)
for i in range(length // 2):
    print(f'{number} = {factor_list[i]} x {factor_list[length-1-i]}')


'''
Quiz.
1. How do you terminate a 'for' loop prematurely in Python?
    a) Using 'break'

2. What is the syntax for a 'for' loop in Python?",
    b. for i in range(5)

3. Which statement is used to skip the current iteration and continue to the next 
in a 'for' loop?
    c) 'continue'

4. What is the maximum number of times a 'for' loop can iterate?",
    d) There is no maximum limit

5. Which data types can be iterated over using a 'for' loop in Python?
    a) Lists and tuples 
    b) Lists and dictionaries
    c) Dictionaries and sets

6. In a 'for' loop, how can you access both the index and value of each element in a list?
    b) Use the enumerate() function
'''