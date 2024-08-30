
name = input("Adinizi daxil edin:\n")
print(name.lower().title())

age = input("yasinizi daxil edin:\n")
print(50-int(age))

address = input("Unvaniniz:\n")
color = input("Sevdiyiniz reng:\n")
car = input("masin:\n")
print(f"""

Unvan: {address}
Sevdiyi reng: {color}
Favorit Brend: {car}

""")


result = ''
digit1 = int(input("Birinci eded:\n"))
digit2 = int(input("ikinci eded:\n"))
operand = input("emeliyyat (+, -, *, /)\n")
if operand =="+":
    result = digit1 + digit2
elif operand == "-":
    result = digit1 - digit2
elif operand == "*":
    result = digit1 * digit2
elif operand == "/":
    result = float(digit1/digit2)
else: print("Xeta")
print(result)

print("(a * b) / c emeliyyati")
digit1 = int(input("Birinci eded:\n"))
digit2 = int(input("ikinci eded:\n"))
digit3 = int(input("Ucuncu eded:\n"))
result = (digit1 * digit2) / digit3
print(f"(a * b) / c = {result}")

print("Ad-Soyadin uzunlugunun tapilmasi")
name = input("Adiniz:\n")
surname = input("Soyadiniz:\n")
fullname = name + " " + surname
print(len(fullname))


print("heqiqi ededin yuvarlaqlasdirilmasi")
x = float(input("heqiqi(noqte ile) eded daxil edin\n"))
round_digit = int(input("Yuvarlasdirilacaq mertebe:\n"))
rounded_x = round(x,round_digit)
print(rounded_x)

print("Quvvetin hesablanmasi\n")
main_number = int(input("Quvveti hesablanacaq tam eded:\n"))
power_number = int(input("Quvvet:\n"))
result = pow(main_number, power_number)
print(result)

print("String center method")
word = input("soz daxil edin\n")
space = int(input("Sahe uzunlugu:\n"))
autofill = input("Bos saheye doldurulacaq simvol:\n")
if autofill == '':
    autofill = ' '
print(word.center(space, autofill))

print("sozun tekrarlanmasi")
repeat_count = int(input("How many times should the program type \"Python\" word?:\n"))
print(repeat_count * "Python")

print("capitalize")
sentence = input("Cumle daxil edin:\n")
print(sentence.upper())

print("replace method")
sentence = input("Cumle daxil edin:\n")
current_char = input("evez edilmeli herf:\n")
while sentence.find(current_char) == -1:
    print("bele simvol yoxdu")
    current_char = input("evez edilmeli herf:\n")
new_char = input("Yeni herf:\n")
print(sentence.replace(current_char, new_char))

print("Lower character checking\n")
word = input("soz daxil edin:\n")
print(word.islower())

print("Digit checking")
word = input("Soz daxil edin:\n")
print(word.isdigit())

print("ifade ve cap sayi")
phrase = input("Ifade daxil edin:\n")
amount = int(input("Cap sayi:\n"))
print(phrase * amount)


print("etrafa * elave etmek")
amount = int(input("Say daxil edin:\n"))
phrase = " Hello world "
print(phrase.center(len(phrase)+2 * amount, "*"))


# Chat GPT's Homework


print("salamlama")
name = input("Insert your name:\n")
print(f"Welcome {name.title()}")

birth_year = int(input("Type your Birth year"))
print(f"You're {2024 - birth_year} years old")

print("Math operations")
x = int(input("First number:\n"))
y = int(input("Second number:\n"))
print(f"Addition: {x + y}")
print(f"Subtraction: {x - y}")
print(f"Multiplication: {x * y}")
print(f"Division: {x / y}")

print("Triangle area")
a = int(input("First side:\n"))
b = int(input("Second side:\n"))
c= int(input("Third side:\n"))
if (a + b) > c and (a + c) > b and (b + c) > a:
    p = (a + b + c) / 2
    s = pow((p * (p - a) * (p - b) * (p - c)), 0.5)
    print("Area: ", s)

else: print("It is not Triangle")

print("Rectangle area")
w =  int(input("wide:\n"))
l = int(input("length:\n"))
s = w * l
print(f"Rectangle area: {s}")

print("Square area")
l = int(input("Square side:\n"))
s = pow(l, 2)
print(f"Square area: {s}")

print("Meter Convert")

distance = float(input("Type distance with meter:\n"))
convert_to_inch = distance * 39.3701
convert_to_feet = distance * 3.28084
print(f"{distance} meter = {convert_to_feet} feet = {convert_to_inch} inch")


# Quiz

"""
1. Which of the following functions is used to convert a value to an integer in Python?
    a) int()

2. When using the input() function in Python, what data type is the input value 
stored as by default?
    c) str

3. You want to find out how many characters are in a user-inputted sentence. 
Which Python function would you use?
    c) len()

4. If a user enters "3.14159" as input using the input() function, how can you 
convert it to a floating-point number?
    a) float(input())

5. If a user enters "5.7" as input using the input() function and you use 
int(input()) for conversion, what will happen?
    a) An error will occur since int() cannot handle decimal values.

6. You want to display the length of a user-inputted string "Hello, World!" with a 
descriptive message. Which option achieves this?
    a) print("The length of the input is:", len(input()))

7. What happens if a user enters "42" as input and you use float(input()) for 
conversion?
    b) The value is converted to the floating-point number 42.0.

8. To style the user prompt and concatenate it with a variable, which option is correct?
    b) input("Enter your name: ") + name

"""

