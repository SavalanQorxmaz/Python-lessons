"""
- Strings -
A. Create a variable called 'long_sentence'. Make it equal a sentence
minimum. Print 'long_sentence's length.
B. Replace Print function's 'end' parameter from default '\n' to '\t'.
Write 2 Print functions with it.
C. Change Print function's 'end' parameter, so that it links values with
stars. Example:
Today*is*a*good*day!
D. Write 3 different Print functions with according string ("He", "is", "cool.")
in such way so you can see this on your console (you can use any method):
He is cool.
E. The same task as previous (D), but now make it look like:
He#is#cool.
F. Create a variable named 'color'. Give it a string 'Python' value.
G. Create a variable named 'item'. Give it a string 'Developer' value.
H. Use all methods you know about string-formattings and Print function
to concatenate these two variables, so you can see 'Python Developer' on your
console (terminal).
I. Replace Print function's 'end' parameter from default value to '...'.
Write 3 Print functions with it.
J. Suppose you have the following variable:
word = "Hello. I am Taylor."

Using slicing method:
1. Create a variable called 'prefix'. Make it equal to 'Hello.' part of 'word' variable.
2. Create a variable called 'middle_part'. Make it equal to ' I am ' part of 'word' variable.
3. Create a variable called 'name'. Make it equal to 'Taylor.' part of 'word' variable.

Create a variable named 'recreated_word' or 'result' and use all previous variables 
(prefix, middle_part, name) to recreate the 'word' phrase.
K. Suppose you have the following value:
"abababababa"

Using slicing method, get all 'a' characters from the value and assign it to a
variable, then print that variable.
L. Create a formula that finds the last index of a string.
M. What is the difference between 1 and "1"? Are they equal values, why?
N. Using all your Python knowledge, find the amount of words the following sentence:
"The mission of the Python Software Foundation is to promote, protect, and advance 
the Python programming language, and to support and facilitate the growth of a 
diverse and international community of Python programmers."

- String Methods -
A. Use all these string methods and test it in your code:
1. title
2. capitalize
3. count
4. endswith
5. find
6. index
7. isalpha
8. isdigit
9. islower
10. isupper
11. lower
12. upper
13. replace
14. split
15. strip
16. startswith
17. join
B. Combine several string methods at once.
C. Create any string-valued variable. First, call the 'lower' method on it,
then call 'islower' method. What value will it always give you and why?
D. Suppose you have the following variable:
my_value = "Obviously, today is a hot day."
Replace all 'o' characters with 0 (zeros). 
E. Count how many times the word 'likes' occured in the following string:
"Sammy likes to swim in the ocean, likes to spin up servers, and likes to smile."

- String Formattings -
A. Create a variable 'name' and assign your name to it.
Create a variable 'age' and assign your age to it.
Using the f-string method, create a formatted string that displays your name 
and age in the following format:
"My name is [name] and I am [age] years old."
B. Create a variable item and assign a string representing an item name.
Create a variable quantity and assign an integer representing the quantity of the item.
Create a formatted string using the old-style % formatting that displays the item 
name and quantity in the following format:
"I want to buy %d units of %s."
C. Make your best and create a hard task by your own using string formattings.

- Chat GPT's Homework -
A. Use the len() function to find the length of the following strings:
1. "programming"
2. "python is fun"
3. "12345"
B. Convert the following string to uppercase string:
"hello world"
C. Check if the string "python" is present in the following sentence:
"I enjoy programming in Python."
D. Given the string "programming", access the following elements using positive and negative indexing:
1. The first character
2. The last character
3. The third character
4. The second-to-last character
E. Using string slicing, extract the word "is" from the string:
"Python is a versatile programming language."
F. Retrieve the substring "quick brown" from the following sentence:
"The quick brown fox jumps over the lazy dog."
G. Reverse the following string using slicing:
"redivider"
H. Write a program that capitalizes the first letter of each word in the following sentence:
"welcome to the world of programming"

- Interview Questions -
A. Reverse any string using slicing method.
B. Print the whole string using slicing method, not knowing the length of a string.

- Comments -
A. One-line comment in any random three places of your code, if it's appropriate.
B. Multi-line comment anywhere in your code, if it's appropriate.

Quiz:
A. What does len('Hello ') return?
    a) 4
    b) 5
    c) 6
    d) 'Hello'
    e) "Hello"

B. What is the output of the following code snippet:

    sphere = "Web Development" * 2 + "" * 6
    length = len(sphere)
    print(length)

    a) 15
    b) 20
    c) 25
    d) 30

C. Which of the operator can be used in Strings?
    a) +
    b) *
    c) Both of the above
    d) None of the above

D. What is the output of the following code snippet:

    comment = "I like your blue pants"
    pattern = comment[19:4:-3]
    print(pattern, len(pattern))

    a) "n lry", 5
    b) "n lry", 4
    c) "n ly", 4
    d) "p ly", 4
    e) "p l ", 4

E. Is the following variable named correctly, why?

    myVariable = "Python is best!"

    a) yes, follows the rules of naming a variable, pythonic code
    b) no, doesn't follow the rules of naming a variable, non-pythonic code
    c) it depends on the code editor you type
    d) it's not a code written in Python
"""