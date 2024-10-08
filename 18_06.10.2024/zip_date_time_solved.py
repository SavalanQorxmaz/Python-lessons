import datetime, time
import calendar
import os
import random
# - Zip (Parallel Iteration) & Enumerate (Counter) -
'''A. Write a program that takes a list and uses the enumerate method to print each 
element in the list along with its index. Use a suitable formatting for the output.
'''
lst = ['a', 'b', 'c', 'd', 'e', 'f']
for i, x in enumerate(lst):
    print(f'{i}: {x}')

'''B. Parallelly iterate over the following collections and print the corresponding
pair values:
students = ["Namig", "Zaur", "Murad", "Aysel"]
gifts = ["Book", "Phone", "Car Model", "Bag"]
'''
students = ["Namig", "Zaur", "Murad", "Aysel"]
gifts = ["Book", "Phone", "Car Model", "Bag"]
pairs = zip(students, gifts)
print(tuple(pairs))

'''C. Iterate over sequence of fruits and print the order of each fruit:
fruits = ["Avocado", "Banana", "Kiwi", "Mango"]
'''
fruits = ["Avocado", "Banana", "Kiwi", "Mango"]
for i, fruit in enumerate(fruits):
    print(f'{i+1}: {fruit}')

'''D. Write a program that takes two lists of equal lengths and uses the zip 
method to create a list of tuples, where each tuple contains elements from both 
lists at the corresponding index. Print the resulting list of tuples.
'''
print('list of tuples')
gifts = ["Book", "Phone", "Car Model", "Bag"]
fruits = ["Avocado", "Banana", "Kiwi", "Mango"]
zipped = zip(fruits, gifts)
for i, (x, y) in enumerate(zipped):
    print(f'{i+1}: {x}-{y}')

# - Date & Time -
'''A. Write a program that prints 'Running...' each 1.5 seconds. The program should
be terminated after 5 executions of the print statement.
'''
i = 5 
while i > 0:
    print('Running...')
    time.sleep(1.5)
    i -=1
else:
    print('Finish')
    
    
'''B. Write a program that uses the datetime module to display the current date and 
time in the format "YYYY-MM-DD HH:MM:SS". Print this information to the console.
'''
now = datetime.datetime.now()
formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
print(formatted_date)

'''C. Write a program that takes a birthdate (year, month, day) and uses the datetime 
module to calculate the age in years.
'''
birthday = datetime.datetime(1989, 2, 15)
now = datetime.datetime.now()
age = now.year - birthday.year
print(f'My age: {age}')

'''D. Write a program calculate_elapsed_time(start_time, end_time) that takes two 
datetime objects representing a start time and an end time. Calculate and return 
the elapsed time in hours, minutes, and seconds.
'''
start_time = datetime.time(5, 59, 59)
end_time = datetime.time(23, 0, 0)
def calculate_elapsed_time(start_time: datetime.time, end_time: datetime.time):
    seconds = end_time.second
    minutes = end_time.minute
    hours = end_time.hour
    if seconds - start_time.second < 0:
        seconds += (60 - start_time.second)
        minutes -= 1
    else:
        seconds -= start_time.second
    if minutes - start_time.minute < 0:
        minutes += (60 - start_time.minute)
        hours -=1
    else:
        minutes -= start_time.minute
    hours -= start_time.hour    
    return (hours, minutes, seconds)  
elapsed_time = datetime.time(*calculate_elapsed_time(start_time, end_time))
print(elapsed_time)

'''E. Write a program that takes a year and a month (1-12) as arguments. Use the calendar 
module to determine and return the number of days in that month.
'''
date = datetime.datetime(2024, 10, 10)
year = date.year
month = date.month
day_count = calendar.monthrange(year, month)[1]
print(day_count)

'''F. Write a program that takes a birthdate (as a datetime object) and calculates the time 
remaining until the next birthday in days, hours, and minutes. Make it in live-clock style.
'''
birthday = datetime.datetime(1989, 2, 15)
next_birthday = datetime.datetime(2025, 2, 15, 0, 0, 1)
now = datetime.datetime.now()

def count_down(days, hours, minutes, secondes)->int:
    return f'{days} Days  {hours}:{minutes}:{secondes}'
# cari ayin qalan gunleri
current_month_rest_days = calendar.monthrange(now.year, now.month)[1] - now.day
print(current_month_rest_days)
# Son ayin qaliq gunleri
last_months_rest_days = next_birthday.day - 1
print(last_months_rest_days)
# Butov aylarin gunleri siyahisi
full_months_days = [calendar.monthrange(now.year, m)[1] for m in range(1,13) if m > now.month] \
+ [calendar.monthrange(next_birthday.year, m)[1] for m in range(1,13) if m < next_birthday.month]
# Butun aylarin gunleri siyahisi
all_days_list = [current_month_rest_days] + full_months_days + [last_months_rest_days]
print(all_days_list)
# Gunlerin cemi
sum_all_days = sum(all_days_list)
# Bu gunun qalan hissesi saat:deqiqe:saniye
rest_time = (23 - now.hour, 59 - now.minute, 60 - now.second)
print(count_down(sum_all_days, *rest_time))
# while True:
#     now = datetime.datetime.now()
#     current_month_rest_days = calendar.monthrange(now.year, now.month)[1] - now.day
#     last_months_rest_days = next_birthday.day - 1
#     full_months_days = [calendar.monthrange(now.year, m)[1] for m in range(1,13) if m > now.month] \
#     + [calendar.monthrange(next_birthday.year, m)[1] for m in range(1,13) if m < next_birthday.month]
#     all_days_list = [current_month_rest_days] + full_months_days + [last_months_rest_days]
#     sum_all_days = sum(all_days_list)
#     rest_time = (23 - now.hour, 59 - now.minute, 60 - now.second)
#     print(count_down(sum_all_days, *rest_time))
#     time.sleep(1)

# Method 2

delta = next_birthday - now
print(delta)

'''G. Write a program that uses the time module to display the current time. However, 
add a delay of 5 seconds using time.sleep(5) before displaying the time.
'''
time.sleep(5)
print(time.ctime())

'''H. Write a program that acts as a countdown timer. Prompt the user to enter a time 
in seconds. Use time.sleep() to create a countdown from the specified time, displaying the 
remaining seconds at each interval of 1 second.
'''
correct = False
seconds = 0
while not correct:
    try:
        seconds = int(input('Enter time with seconds: '))
        if seconds > 0:
            correct = True
        else:
            print('Only positive number')
    except ValueError:
        print('Incorrect format')
print(seconds)
while seconds > 0:
    os.system('cls')
    print(f'Last {seconds} seconds')
    seconds -= 1
    time.sleep(1)
else:
    os.system('cls')
    print('End....')

'''I. Write a program that displays the current time every minute. Use a loop and time.sleep() 
to achieve this. The program should display the time at each minute interval.
'''
index = 1
while index < 10:
    os.system('cls')
    now = datetime.datetime.now()
    print(now)
    index += 1
    time.sleep(60)

'''J. Write a program that displays a random message every 2 to 5 seconds. Use the random 
module to select a random message from a predefined list and display it to the
'''
messages = ['Hello', 'Bye', 'Ok', 'None']
for _ in range(5):
    interval = random.randrange(2, 5)
    print(f'New message after {interval} seconds')
    time.sleep(interval)
    message = random.choice(messages)
    print(message)

'''K. Write a program in style of "Squid Game". First, create a list of ten random numbers.
Then, every 10 seconds remove (kill) the smallest value from the list.
'''
print('Squid Game')
lst = [random.randint(0, 100) for _ in range(10)]
while len(lst) > 0:
    print(lst)
    smallest = min(lst)
    lst.pop(lst.index(smallest))
    time.sleep(10)


# - Chat GPT's Homework -
'''1. Write a program that uses the zip method to create a new list of tuples,
where each tuple contains elements from both lists at the corresponding 
index.
'''
lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lst2 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
zip_lst = zip(lst1, lst2)
print(*zip_lst)


'''2. Write a program that takes two lists, keys and values and uses the zip 
method to create a dictionary where the elements from the keys list are the 
keys and the elements from the values list are the corresponding values. 
'''
keys_list = ['name', 'surname', 'age']
values_list = ['Ali', 'Aliyev', 25]
zip_list = zip(keys_list, values_list)
dict_zip = dict(zip_list)
print(dict_zip)


'''3. Write a program that takes an iterable and an optional starting index 
(default is 0). Implement the functionality of enumerate using a loop, and 
return a list of tuples where each tuple contains the index (starting from 
the provided start) and the corresponding element from the iterable.
'''
lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
index_value_list = [(i, x) for (i, x) in enumerate(lst)]
print(index_value_list)


'''4. Explain the difference between the time() method and the sleep() method 
in the time module. Provide use cases for each.
'''
index = 1
while index < 10:
    print(time.time()) 
    index += 1
    time.sleep(1)


'''5. Describe the purpose and functionality of the strftime() method in the 
datetime module. Provide an example of how to use it.
'''
now = datetime.datetime.now()
print(now.strftime('%Y %B %d'))


'''6. Explain the significance of the epoch time (January 1, 1970) and how it's 
related to the time() method in the time module.
'''
now = time.time()
delta = datetime.timedelta(milliseconds=now)
print('delta', delta)
print(now)


'''7. What is the purpose of the timedelta class in the datetime module? Provide 
an example use case where timedelta can be helpful.
'''
last_day = datetime.datetime(2025, 2, 15)
now = datetime.datetime.now()
delta = last_day - now
print(delta)
rest_time = delta.total_seconds()
print(rest_time)

# Quiz.
'''1. The datetime module in Python provides a class for manipulating dates 
and times. What is the name of this class?
    d) datetime

2. Which method in the datetime module returns the current date and time?
    b) now()

3. In the strftime method, what does %Y represent in the formatting string?
    b) Year (e.g., 2023)

4. Which module in Python provides functionality to work with time-related 
operations such as measuring time intervals, and converting between different 
time representations?
    a) time

5. Which method from the time module returns the current time in seconds since 
the epoch (January 1, 1970)?
    a) time()

6. In the time module, which method pauses the program's execution for the specified 
number of seconds?
    a) sleep()

7. Which method of the datetime class in the datetime module returns a formatted string 
representing the date and time?
    b) strftime()

8. In the datetime module, what does the timedelta class represent?
    a) A duration expressing the difference between two date or time instances

9. Which method of the timedelta class allows you to extract the number of days?
    b) total_days()

10. To get the current date and time, which method would you use in the datetime module?
    a) datetime.now()

11. In the strftime method, what does %d represent in the formatting string?
    c) Day of the month (01-31)

12. In the strftime method, what does %H represent in the formatting string?
    c) Hour (00-23)

13. In the strftime method, what does %M represent in the formatting string?
    c) Minute (00-59)

14. Consider the following Python code snippet:
    import time

    start_time = time.time()
    time.sleep(3)
    end_time = time.time()

    print(f"Execution took {end_time - start_time} seconds.")

    What is the purpose of this code, and what will be the output when it is executed?
    b) This code creates a timer that prints "Execution took 3 seconds." 
    after waiting for 3 seconds.

'''