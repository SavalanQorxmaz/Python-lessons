# String Formattings

genre = "Mugam"
producer = "Alim Gasimov"
song= "Deshti"

fstring_method = f"{producer} best singer {genre}'s {song}"
print(f"F-String method:\n{fstring_method}")

format_method = "{} best singer {}'s {}".format(producer, genre, song)
print("Format method:\n {}".format(format_method))

s_method = "%s best singer %s's %s" % (producer, genre, song)
print("%S method:\n " + s_method)

firstname = "Ali"
lastname = "Aliyev"
age = 25
gender = "Male"

# ----------------------------------------------------------------
userinfo_fstring = f"__Fstring Method: \nMy name is {firstname} {lastname}, and I am {age} years old. My gender is {gender}."
print(userinfo_fstring)

userinfo_format = "__Format Method: \nMy name is {} {}, and I am {} years old. My gender is {}.".format(firstname, lastname, age, gender)
print(userinfo_format)

userinfo_s = "__S Method: \nMy name is %s %s, and I am %s years old. My gender is %s." % (firstname, lastname, age, gender)
print(userinfo_s)

# -----------------------------------------------------------------
language = "Python"

python_lover = f"I love {language}. I will repeat this word 5 times: {language * 5}."
print(python_lover)

# ----------------------------------------------------------------
word1 = "hello"
word2 = "world"

word1_title1 = word1.title()
word2_title1 = word2.title()
words_concat1 = word1_title1 + " " + word2_title1

word1_title2 = word1.replace("h", "H")
word2_title2 = word2.replace("w", "W")
words_concat2 = word1_title2 + " " + word2_title2

word1_title3 = word1[0].upper() + word1[1:]
word2_title3 = word2[0].upper() + word2[1:]
words_concat3 = "{} {}".format(word1_title3, word2_title3)



print(f"Title method:\n {words_concat1}\nReplace method:\n {words_concat2}\nConcat method:\n {words_concat3}")

# -----------------------------------------------------------------

hello = "15.02.1989"
print("My birth date is %s." % hello)


all_variables = f"""
All variables:
{genre=}
{producer=}
{song=}
{firstname=}
{lastname=}
{age=}
{gender=}
{language=}
{hello=}

"""
print(all_variables)

# ----------------------------------------------------------------

sentence = "{} {} {} {}"
word1 = "My"
word2 = "favorite"
word3 = "poet"
word4 = "Camus"
filled_sentence = sentence.format(word1, word2, word3, word4)
print("filled sentence:\n", filled_sentence)

# ----------------------------------------------------------------

x = 5
y = 8
operations= f"Addition: {x + y}\nSubtraction Module: {abs(x-y)}\nMultiplication: {x * y}\nDivision: {(x / y):.2f}"

print(operations)

# ---------------------------------------------------------------

expression = "JavaScript"

replayed_expression = sentence.format(expression, expression, expression, expression)
print("replayed expression: ",replayed_expression)

# ---------------------------------------------------------------


"""
A. In the following code, 'Hello' is a string literal. True or false?

    ---------------------
    |    s = 'Hello'    | 
    ---------------------

    a) True

B. The two strings 'Hello' and "Hello" are identical to each other. Yes or no?
    a) Yes

C. Is there a problem in the code below? If yes, then how can we rectify it?

    ------------------------------
    |    s = 'Python's call!'    | 
    ------------------------------

    b) Yes, by using a backslash


D. How to denote a multiline string in Python?

    c) Using either (b) and (c)



E. When used on strings, what does the * operator do?
    a) Replicates them
    
"""