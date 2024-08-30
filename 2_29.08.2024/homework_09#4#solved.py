long_sentence = "it is Friday"
print(len(long_sentence))

# -----------------------------------------

print("First print function", end = "\t")
print("Second print function")

print("Today", "is", "a", "good", "day!", sep="*")

print("He", end= ' ')
print("is", end= ' ')
print("cool.")

print("He", end= '#')
print("is", end= '#')
print("cool.")

# -------------------------------------------

color = "Python"
item = "Developer"

print(f"F-String method: {color} {item}")
print("Format method: {} {}".format(color, item))
print("s method: %s %s" % (color, item))

# ---------------------------

print("He",end= "...")
print("She", end= "...")
print("It", end= "...")


# ---------------------------------------
print()
word = "Hello. I am Taylor."

prefix = word[:5]
middle_part = word[6:12]
name = word[-7:-1]

result = f"{prefix=}\n{middle_part=}\n{name=}"

print(result)

# ---------------------------------------

word = "abababababa"
only_a = word[::2]
print(only_a)

last_index = len(word)-1
print(last_index)

difference = f"""

1 is {type(1)}
"1" is {type("1")}

"""
print(difference)

# -------------------

long_sentence = """The mission of the Python Software Foundation is to promote, protect, and advance 
the Python programming language, and to support and facilitate the growth of a 
diverse and international community of Python programmers."""

print("Title method:",long_sentence.title())
print("Capitalize method:",long_sentence.capitalize())
print("Count a:",long_sentence.count("a"))
print("Endswith method:",long_sentence.endswith("programmers."))
print("Find method:",long_sentence.find("Python"))
print("Index method:",long_sentence[12])
print("Alphabet method:",long_sentence.isalpha())
print("Isdigit method:",long_sentence.isdigit())
print("Islower method:",long_sentence.islower())
print("Isupper method:",long_sentence.isupper())
print("Upper method:",long_sentence.upper())
print("Lower method:",long_sentence.lower())
print("Replace method:",long_sentence.replace("Python", "Javascript"))
print("Split method:",long_sentence.split(" "))
print("Strip method:",long_sentence.strip())
print("Startswidth method:",long_sentence.startswith("The"))
print("Join method:","-".join(long_sentence.split(" ")))


print(long_sentence.lower()[::2])
print(long_sentence.split(" ")[5])


sentence = "Python Software Foundation"
print(sentence.lower())
print(sentence.lower().islower())


my_value = "Obviously, today is a hot day."
new_value = my_value.replace("o", "0")
print(new_value)


sentence = "Sammy likes to swim in the ocean, likes to spin up servers, and likes to smile."
like_count = sentence.count("likes")
print(like_count)


name = "Savalan"
age = 35
i_am = f"My name is {name} and I am {age} years old."
print(i_am)

fruit = "Apple"
quantity = 5
i_want = "I want to buy %dkq units of %s." % (quantity, fruit)
print(i_want)


# --------------------------------------------------

print(f"len(\"programming\"): {len("programming")}")
print(f"len(\"python is fun\"): {len("python is fun")}")
print(f"len(\"12345\"): {len("12345")}")

print(f"\"hello world\" uppercase: {"hello world".upper()}")

print(f"{"I enjoy programming in Python.".lower().find("python")}")

print(f"First: {"programming"[0]}")
print(f"Last: {"programming"[len("programming")-1]}")
print(f"2nd: {"programming"[2]}")
print(f"2nd negative index: {"programming"[-len("programming")+2]}")

print(f"1-end: {"programming"[1:]}")

sentence = "Python is a versatile programming language."
print(f"Method1: {sentence.replace(" is", "")}")
print(f"Method2: {sentence[:sentence.find(" is")] + sentence[sentence.find(" is")+3:]}")

sentence = "The quick brown fox jumps over the lazy dog."
print(sentence[4:15])

word = "redivider"
reversed_word = word[::-1]
print(reversed_word)


sentence = "welcome to the world of programming"

sentence_capitalize = sentence.title()
print(sentence_capitalize)


# Interview Questions

"""
A) string[::-1]

B) print(string[:])



"""

# Quiz

"""

A. What does len('Hello ') return?
    c) 6


B. What is the output of the following code snippet:

    sphere = "Web Development" * 2 + "" * 6
    length = len(sphere)
    print(length)

    d) 30


C. Which of the operator can be used in Strings?
    c) Both of the above

D. What is the output of the following code snippet:

    comment = "I like your blue pants"
    pattern = comment[19:4:-3]
    print(pattern, len(pattern))

    a) "n lry", 5

E. Is the following variable named correctly, why?

    myVariable = "Python is best!"

    b) no, doesn't follow the rules of naming a variable, non-pythonic code
    d) it's not a code written in Python

"""