import time
import random
#   - While Loops -

print('''A. Write a program that asks user for a number between 100 and 500. The program should ask the user
until he/she enters the number within a given range.
''')
correct = False
while not correct:
    user_input = input("Enter number between 100-500: ").strip()
    try: 
        number = int(user_input)
        if 100 <=number <= 500:
            print(f'Your number is: {number}')
            correct = True
        else:
            print(f'wrong diapason {number}')
    except:
        print(f'Incorrect format: {user_input}')
        
print('''B. Write a program that prints even and odd numbers between 1 to the entered number.
''')
correct = False
evens = [ ]
odds = [ ]
while not correct:
    user_input = input("Number: ").strip()
    try: 
        number = int(user_input)
        step = 1
        while step <= number:
            if step % 2 == 0:
               evens.append(str(step))
            else:
               odds.append(str(step))
            step += 1
        correct = True
    except:
        print(f'Incorrect format: {user_input}')
print(f'Evens: {', '.join(evens)}\nOdds: {', '.join(odds)}')

print('''C. Write a program to display each character from a string and if a 
character is number then stop the loop.
''')
word = 'he is 18 years old'
length = len(word)
step = 0
while step < length:
    if word[step].isdigit():
        print(word[0:step])
        break
    else:
        print(word[step])
        step += 1

print('''D. Write a program to calculate the sum of series up to n term. For example, 
if n=5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690
''')
correct = False
lst = [ ]
while not correct:
    user_input = input("Enter number: ").strip()
    try: 
        number = int(user_input)
        step = 1
        while step <= number:
            item = '2' * step
            lst.append(int(item))
            step += 1
        correct = True    
    except:
        print(f'Incorrect format: {user_input}')
total = sum(lst)
print(f'Sum: {lst} = {total}')

print('''E. Create a program that prompts the user to enter a number, 
then use a while loop to count from 1 up to the user's number.
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
step = 1
while step <= number:
    print(step)
    step += 1
    
print('''F. Write a Python program that uses a while loop to print numbers from 1 to 10.
''')
step = 1
while step <= 10:
    print(step)
    step += 1

print('''G. Write a program that checks if a user-entered string is a palindrome (reads the same forwards 
and backwards) using a while loop. Ignore spaces and letter case.
''')
word = input('Enter word: ').strip().lower()
word_without_space = ''.join([x for x in word if x != ' '])
is_polindrome = True
step = 0
length = len(word_without_space)
while step < length // 2 + 1:
    if word_without_space[step] == word_without_space[length - step - 1]:
        step += 1
    else:
        is_polindrome = False
        break
print(f'{word} is polindrome') if is_polindrome else print(f'{word_without_space} is not polindrome')


print('''H. Write a program that asks the user for an integer. If the number is even, divide it by 2, 
if it's odd, multiply it by 3 and add 1. Repeat this process with the result until the result 
becomes 1, and count how many steps it took.
''')
number = None
correct = False
step_operation = [ ]
while not correct:
    user_input = input("Enter number: ").strip()
    try: 
        number = int(user_input)    
        correct = True
    except:
        print(f'Incorrect format: {user_input}')
while number != 1:
    if number % 2 == 0:
        number = number // 2
    else:
        number = number * 3 + 1
    step_operation.append(number)
print(f'step count: {len(step_operation)}\nstep operation: {step_operation}')

print('''I. Create a program that calculates the sum of all even numbers from 1 to a user-specified 
number using a while loop.
''')
number = None
correct = False
evens_total = 0
while not correct:
    user_input = input("Enter number: ").strip()
    try: 
        number = int(user_input)    
        correct = True
    except:
        print(f'Incorrect format: {user_input}')
step = 1
while step <= number:
    if step % 2 == 0:
        evens_total += step
    step += 1
print(f'{evens_total = }')
        
print('''J. Create a program that takes a list of numbers as input and reverses the list using a while loop. 
Do this without using any built-in list reversal methods.
''')
number = None
correct = False
lst = [ ]
rvrs_lst = [ ]
while not correct:
    print('If you want stop, write other character')
    user_input = input("Enter number: ").strip()
    try: 
        number = int(user_input)    
        lst.append(number)
    except:
        correct = True
length = len(lst)
step = 0
while step < length:
    rvrs_lst.insert(0, lst[step])
    step += 1
print(f'List: {lst}\nReversed list: {rvrs_lst}')

# - Extra Hard -
print('''Task A. Count the total number of digits in a number. If user enters 547,
the program should add each digit, so the output is 16 (as 5 + 4 + 7 = 16).
''')
number = None
user_input = None
correct = False
while not correct:
    user_input = input("Enter number: ").strip()
    try: 
        number = int(user_input)    
        correct = True
    except:
        print(f'Incorrect format: {user_input}')

# Method 1
total = 0
while number != 0:
    total += number % 10
    number = number // 10
print(f'Total= {total}')

# Method 2
total = 0
while len(user_input) > 0:
    total += int(user_input[-1])
    user_input = user_input[:-1]
print(f'Total= {total}')

print('''Task B. Write a program to display all prime numbers within a range.
''')
number = None
correct = False
primes = [ ]
while not correct:
    user_input = input("Enter number: ").strip()
    try: 
        number = int(user_input)    
        correct = True
    except:
        print(f'Incorrect format: {user_input}')
step = 0
while step <= number:
    is_prime = False
    while not is_prime:
        for i in range(2, step):
            if step % i == 0:
                primes.append(step)
                break
        is_prime = True
    step +=1
print(primes)
        

print('''Task C. Create a program that takes a string as input and uses a while loop to reverse 
and print the characters of the string.
''')
word = input('Word: ')
length = len(word) - 1
while length >= 0:
    print(word[length])
    length -= 1

print('''Task D. Write a program that checks if a user-entered string is a palindrome (reads the 
same forwards and backwards) using a while loop. Ignore spaces and letter case.
''')
word = input('Enter word: ').strip().lower()
word_without_space = ''.join([x for x in word if x != ' '])
step = 0
is_polindrome = True
length = len(word_without_space)
while step < length // 2 + 1:
    if word_without_space[step] == word_without_space[length - step - 1]:
        step += 1
    else:
        is_polindrome = False
        break
if is_polindrome:
    print(f'{word} is polindrome')
else:
    print(f'{word_without_space} is not polindrome')

print('''Task E. Develop a program that takes an integer as input and prints a number pyramid using a 
while loop. For example, if the user enters 5, the program should print:
    1
   121
  12321
 1234321
123454321
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
step = 1
while step <= number:
    row = ''
    i = 1
    while i < step:
        row += str(i)
        i += 1
    row = row + str(step) + row[::-1]
    print(row.center(number * 2))
    step += 1
        
    
# - Chat GPT's Homework -
'''Task 1: Countdown Timer
Write a program that uses a while loop to create a countdown timer. 
Ask the user to enter a number of seconds, and then display a countdown 
from that number down to 0.
'''
print('Countdown Timer')
number = None
correct = False
while not correct:
    user_input = input("Enter number: ").strip()
    try: 
        number = int(user_input)    
        correct = True
    except:
        print(f'Incorrect format: {user_input}')
while number > 0:
    print(f'Start after {number} second')
    time.sleep(1)
    number -= 1
else:
    print('Start....')        

'''Task 2: Number Guessing Game
Create a number guessing game where the computer generates a random number, 
and the user has to guess it. Use a while loop to allow the user to keep 
guessing until they correctly guess the number.
'''
print('Number Guessing Game')

random_number = random.randrange(1, 9)
number = None
correct = False
while not correct:
    user_input = input("Enter number between 1-10: ").strip()
    try: 
        number = int(user_input) 
        if 1 <=number <= 10:
            if number == random_number:
                print('You win')
            else:
                print(f'Your number is: {number}\nSystem number is {random_number}\nYou loss')
            correct = True
        else:
            print(f'wrong diapason {number}')  
    except:
        print(f'Incorrect format: {user_input}')

'''Task 3: Factorial Calculator
Write a program that calculates the factorial of a given number using a while 
loop. Ask the user for an integer input and compute its factorial.
'''
print('Factorial Calculator')
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

'''Task 4: Password Validation
Implement a program that asks the user to enter a password. Use a while loop 
to keep asking for the password until it matches a predefined correct password.
'''
print('Password Validation Current password(123)')
password = '123'
user_input = input('Enter pasword: ')
while user_input != password:
    user_input = input('Password wrong, type again: ')
else:
    print('Welcome!')


'''Task 6: Sum of Even Numbers
Calculate and display the sum of all even numbers from 1 to a user-defined 
upper limit using a while loop.
'''
print('Sum of Even Numbers')
number = None
correct = False
while not correct:
    user_input = input("Enter number: ").strip()
    try: 
        number = int(user_input) 
        correct = True 
    except:
        print(f'Incorrect format: {user_input}')
step = 1
total = 0
while step <= number:
    if step % 2 == 0:
        total += step
    step += 1
print(f'{total = }')

'''Task 7: Multiplication Table
Generate and display the multiplication table for a given number using a while 
loop. Ask the user for the number and the range (e.g., 1 to 10).
'''
print('Multiplication Table')
user_dict = {
    'number': None,
    'start': None,
    'stop': None
    }
for x in list(user_dict.keys()):
    correct = False
    while not correct:
        print(f'Enter {x}: ')
        user_input = input().strip()
        try: 
            user_dict.update({x: int(user_input)})
            correct = True 
        except:
            print(f'Incorrect format: {user_input}')
if user_dict['start'] > user_dict['stop']:
    print(f'Start > stop: Their prices were exchanged with each other')
    temp = user_dict['start']
    user_dict.update({'start': user_dict['stop'], 'stop': temp})
print(user_dict)
step = user_dict['start']
while step <= user_dict['stop']:
    print(f'{user_dict["number"]} X {step} = {user_dict["number"] * step}')
    step += 1

'''Task 8: Pattern Printing
Write a program that uses a while loop to print a pattern of asterisks, 
where the number of asterisks on each line is equal to the line number. 
For example:
*
**
***
****
*****
'''
print('Pattern Printing')
number = None
correct = False
while not correct:
    user_input = input("Enter number: ").strip()
    try: 
        number = int(user_input) 
        correct = True 
    except:
        print(f'Incorrect format: {user_input}')
row = 1
while row <= number:
    print(row * '*')
    row += 1

'''Task 9: Task with a for loop
Create a program that uses both while and for loops. Ask the user for a number 
and print its multiplication table using a for loop inside the while loop. 
Continue asking for numbers until the user enters '0' to exit.
'''
print('Task with a for loop')
finish = None
while finish != 0:
    number = None
    correct = False
    while not correct:
        user_input = input("Enter number, if you want exit, type 0: ").strip()
        try: 
            number = int(user_input) 
            if number == 0:
                finish = 0
            else:
                for num in range(1, 11):
                    print(f'{num} x {number} = {num * number}')
            correct = True 
        except:
            print(f'Incorrect format: {user_input}')
print('You exit')
        
'''
Quiz.
1. What is the primary purpose of a while loop in Python?
    c) To repeatedly execute a block of code as long as a specified condition remains true.

2. What are some best practices for using while loops in Python?
    a) Always initialize loop control variables within the loop.
    d) Use meaningful variable names and prevent infinite loops.

3. What should you consider when using a while loop in Python?
    a) Potential performance impact.
    b) Using while loops for known iterations.
    d) Using while loops for all types of iterations.

4. What are the key differences between while and for loops in Python?

5. What is the potential risk of using an infinite while loop in your code?
    b) It can lead to unexpected program termination.
    
6. How do you ensure that a while loop will terminate and not result in an infinite loop?
    b) By initializing loop control variables within the loop.

7. Which of the following statements is true about the loop control variable in a while loop?
    c) It is used to define the loop condition and manage loop execution.

8. In Python, what happens when the condition of a while loop is initially False?
    c) The loop executes at least once.

9. What is an off-by-one error in the context of while loops?
    b) An error that happens when a loop runs one more or one less time than intended.

10. What is the output of the following code?
    count = 1
    while count <= 5:
        print(count)
        count += 1

    a) 1 2 3 4 5

11. What is the output of the following code?
    while True:
        print("Infinite Loop")

    a) Infinite Loop

12. What is the output of the following code?
    count = 1
    while count <= 10:
        if count == 5:
            break
        print(count)
        count += 1

    b) 1 2 3 4

13. What is the output of the following code?
    count = 1
    while count <= 5:
        if count % 2 == 0:
            count += 1
            continue
        print(count)
        count += 1

    b) 1 3 5

14. What is the output of the following code?
    outer_count = 1
    while outer_count <= 3:
        inner_count = 1
        while inner_count <= 2:
            print(outer_count, inner_count)
            inner_count += 1
        outer_count += 1

    e) None of the above

15. What is the output of the following code?
    num = 5
    fact = 1
    while num > 0:
        fact *= num
        num -= 1
    print(fact)

    a) 120

16. What is the output of the following code?
    total = 0
    while True:
        num = int(input("Enter a number (0 to exit): "))
        if num == 0:
            break
        total += num
    print("Sum:", total)

    a) The program adds numbers until the user enters 0 and then displays the sum.

17. What is the value of x:
    x = 0
    while (x < 100):
        x += 2
        print(x)

    d) 100

18. What is the output of the following if statement
    a, b = 12, 5
    if a + b:
        print('True')
    else:
        print('False')

    b) True

19. What is the value of the var after the for loop completes its execution:
    var = 10
    for i in range(10):
        for j in range(2, 10, 1):
            if var % 2 == 0:
                continue
                var += 1
        var+=1
    else:
        var+=1

    b) 21

20. What is the output of the following nested loop:
    for num in range(10, 14):
        for i in range(2, num):
            if num%i == 1:
                print(num)
                break

    a)
    10
    11
    12
    13

21. What is the output of the following nested loop:
    numbers = [10, 20]
    items = ["Chair", "Table"]

    for x in numbers:
        for y in items:
            print(x, y)

    a)
    10 Chair
    10 Table
    20 Chair
    20 Table
'''
