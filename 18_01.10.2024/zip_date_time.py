"""
- Zip (Parallel Iteration) & Enumerate (Counter) -
A. Write a program that takes a list and uses the enumerate method to print each 
element in the list along with its index. Use a suitable formatting for the output.
B. Parallelly iterate over the following collections and print the corresponding
pair values:
students = ["Namig", "Zaur", "Murad", "Aysel"]
gifts = ["Book", "Phone", "Car Model", "Bag"]
C. Iterate over sequence of fruits and print the order of each fruit:
fruits = ["Avocado", "Banana", "Kiwi", "Mango"]
D. Write a program that takes two lists of equal lengths and uses the zip 
method to create a list of tuples, where each tuple contains elements from both 
lists at the corresponding index. Print the resulting list of tuples.

- Date & Time -
A. Write a program that prints 'Running...' each 1.5 seconds. The program should
be terminated after 5 executions of the print statement.
B. Write a program that uses the datetime module to display the current date and 
time in the format "YYYY-MM-DD HH:MM:SS". Print this information to the console.
C. Write a program that takes a birthdate (year, month, day) and uses the datetime 
module to calculate the age in years.
D. Write a program calculate_elapsed_time(start_time, end_time) that takes two 
datetime objects representing a start time and an end time. Calculate and return 
the elapsed time in hours, minutes, and seconds.
E. Write a program that takes a year and a month (1-12) as arguments. Use the calendar 
module to determine and return the number of days in that month.
F. Write a program that takes a birthdate (as a datetime object) and calculates the time 
remaining until the next birthday in days, hours, and minutes. Make it in live-clock style.
G. Write a program that uses the time module to display the current time. However, 
add a delay of 5 seconds using time.sleep(5) before displaying the time.
H. Write a program that acts as a countdown timer. Prompt the user to enter a time 
in seconds. Use time.sleep() to create a countdown from the specified time, displaying the 
remaining seconds at each interval of 1 second.
I. Write a program that displays the current time every minute. Use a loop and time.sleep() 
to achieve this. The program should display the time at each minute interval.
J. Write a program that displays a random message every 2 to 5 seconds. Use the random 
module to select a random message from a predefined list and display it to the
K. Write a program in style of "Squid Game". First, create a list of ten random numbers.
Then, every 10 seconds remove (kill) the smallest value from the list.

- Chat GPT's Homework -
1. Write a program that uses the zip method to create a new list of tuples,
where each tuple contains elements from both lists at the corresponding 
index.

2. Write a program that takes two lists, keys and values and uses the zip 
method to create a dictionary where the elements from the keys list are the 
keys and the elements from the values list are the corresponding values. 

3. Write a program that takes an iterable and an optional starting index 
(default is 0). Implement the functionality of enumerate using a loop, and 
return a list of tuples where each tuple contains the index (starting from 
the provided start) and the corresponding element from the iterable.

4. Explain the difference between the time() method and the sleep() method 
in the time module. Provide use cases for each.

5. Describe the purpose and functionality of the strftime() method in the 
datetime module. Provide an example of how to use it.

6. Explain the significance of the epoch time (January 1, 1970) and how it's 
related to the time() method in the time module.

7. What is the purpose of the timedelta class in the datetime module? Provide 
an example use case where timedelta can be helpful.

Quiz.
1. The datetime module in Python provides a class for manipulating dates 
and times. What is the name of this class?
    a) Datetime
    b) Date
    c) Time
    d) datetime

2. Which method in the datetime module returns the current date and time?
    a) current()
    b) now()
    c) today()
    d) get_current_datetime()

3. In the strftime method, what does %Y represent in the formatting string?
    a) Month (01-12)
    b) Year (e.g., 2023)
    c) Day of the week (Monday-Sunday)
    d) Hour (00-23)

4. Which module in Python provides functionality to work with time-related 
operations such as measuring time intervals, and converting between different 
time representations?
    a) time
    b) datetime
    c) timedelta
    d) timezone

5. Which method from the time module returns the current time in seconds since 
the epoch (January 1, 1970)?
    a) time()
    b) ctime()
    c) strftime()
    d) gmtime()

6. In the time module, which method pauses the program's execution for the specified 
number of seconds?
    a) sleep()
    b) wait()
    c) pause()
    d) delay()

7. Which method of the datetime class in the datetime module returns a formatted string 
representing the date and time?
    a) format()
    b) strftime()
    c) to_string()
    d) get_formatted()

8. In the datetime module, what does the timedelta class represent?
    a) A duration expressing the difference between two date or time instances
    b) A specific point in time
    c) A formatted date and time string
    d) A timezone offset

9. Which method of the timedelta class allows you to extract the number of days?
    a) days()
    b) total_days()
    c) get_days()
    d) days_total()

10. To get the current date and time, which method would you use in the datetime module?
    a) datetime.now()
    b) datetime.today()
    c) datetime.current()
    d) datetime.get_current()

11. In the strftime method, what does %d represent in the formatting string?
    a) Month (01-12)
    b) Year (e.g., 2023)
    c) Day of the month (01-31)
    d) Hour (00-23)

12. In the strftime method, what does %H represent in the formatting string?
    a) Month (01-12)
    b) Year (e.g., 2023)
    c) Hour (00-23)
    d) Minute (00-59)

13. In the strftime method, what does %M represent in the formatting string?
    a) Month (01-12)
    b) Year (e.g., 2023)
    c) Minute (00-59)
    d) Second (00-59)

14. Consider the following Python code snippet:
    import time

    start_time = time.time()
    time.sleep(3)
    end_time = time.time()

    print(f"Execution took {end_time - start_time} seconds.")

    What is the purpose of this code, and what will be the output when it is executed?
    a) This code measures the execution time of the time.sleep(3) statement 
    and prints the elapsed time in seconds.
    b) This code creates a timer that prints "Execution took 3 seconds." 
    after waiting for 3 seconds.
    c) This code will throw an error because time.sleep() cannot be used 
    with a floating-point argument.
    d) This code will hang indefinitely without producing any output.
"""