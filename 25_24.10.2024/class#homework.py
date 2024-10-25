
import unittest
import logging

logging.basicConfig(
    level=logging.NOTSET,
    # filename='class_log.log',
    filemode='w',
    format="%(asctime)s    %(levelname)s   %(message)s"
)

info = logging.info

# Homework Assignment: Introduction to Classes in Python

# Instructions:
# Create a Python program with two classes that model real-world objects. 
# Each class should have attributes, methods, and a main program that demonstrates 
# their functionality. Follow the steps below to complete the assignment.

# Class 1: Person

# Create a class named Person with the following attributes and methods:

# Attributes:

# name (str) - The name of the person.
# age (int) - The age of the person.

# Methods:

# greeting(self) - A method that prints a greeting message using the person's name.
# sleep(self) - A method that prints a message indicating that the person is going to sleep.

# Class 2: Animal

# Create a class named Animal with the following attributes and methods:

# Attributes:

# name (str) - The name of the animal.
# age (int) - The age of the animal.
# color (str) - The color of the animal
# Methods:

# eat(self) - A method that prints a message indicating that the animal is going to eat.
# run(self) - A method that prints a message indicating that the animal is running.

# Main Program:

# Write a main program that demonstrates the use of the Person and Animal classes. 
# Create instances of both classes and use their methods to show their behavior. 
# For example, create a person and an animal, set their attributes, and call 
# their appropriate methods for each of them.

# Ensure that your program is well-documented and follows best practices for Python 
# code formatting and style.

class Person:
    def __init__(self, name:str, age:int) -> None:
        self.name = name
        self.age = age
        
    def greeting(self):
        info(f'Hello, {self.name}')
        
    def sleeping(self):
        info(f'{self.name} went to sleep....')
    
class Animal:
    def __init__(self, **kwargs) -> None:
        self.name = kwargs['name']
        self.age = kwargs['age']
        self.color = kwargs['color']
        
    def eat(self):
        info(f'{self.name} eating...')
    
    def run(self):
        info(f'{self.name} is running')
        
bob = Person('Bob', 20)

tarzan = Animal(name='Tarzan', age=2, color='gray')

bob.greeting()
tarzan.eat()

# Inheritance
class Alive:
    def __init__(self, name, age, **kwargs) -> None:
        self.name = name
        self.age = age
        
class PersonInh(Alive):
    def greeting(self):
       return f'Hello, {self.name}'
        
    def sleeping(self):
        return f'{self.name} went to sleep....'

class AnimalInh(Alive):
    def __init__(self, name, age, **kwargs) -> None:
        super().__init__(name, age, **kwargs)
        self.color = kwargs['color']
    def eat(self):
       return f'{self.name} eating...'
    
    def run(self):
        return f'{self.name} is running'
        
mark = PersonInh('Mark', 25)
lucy = PersonInh('Lucy', 30)
info(mark.sleeping())
mastan = AnimalInh('Mastan', 2, color='white')

info(mastan.eat()) 

'''Quiz.

1. What is a class in Python?
    b) A class is an instance of an object.
    c) A class is a blueprint for creating objects.

2. In Python, which keyword is used to define a class?
    a) class

3. How do you create an instance of a class in Python?
    b) By calling the class as a function.
    
4. Which of the following statements is true regarding attributes in a class?
    c) Attributes are variables that store data in a class.

5. Which keyword is used to access the attributes and methods of a class instance?
    d) dot (.)
    
6. How do you create an instance of a class in Python?
    b) By calling the class as a function.
    
7. Which of the following statements is true regarding attributes in a class?
    b) Attributes are variables that store data in a class.
    
8. What is an "object" in the context of classes?
    a) An instance of a class.

9. What is the relationship between a class and an object in Python?
    b) An object is an instance of a class.
    
10. What are "attributes" in a class?
    b) Variables that store data within a class.
    
11. In Python, how do you define a class?
    a) By using the class keyword followed by the class name and a colon.
    '''
    
class TestClass(unittest.TestCase):
    def test_person(self):
        person1 = Person('Person1', 30)
        self.assertIsNone(person1.greeting())
    def test_animal(self):
        animal1 = Animal(name='Animal1', age=3, color='black')
        self.assertEqual(animal1.eat(), None)
    def test_alive(self):
        alive = Alive('Dog', 1)
        self.assertEqual(alive.age, 1)
    def test_personinh(self):
        corc = PersonInh('Corc', 40)
        self.assertEqual(corc.sleeping(), f'{corc.name} went to sleep....')
    def test_animalinh(self):
        cat = AnimalInh('Cat', 40, color = 'white')
        self.assertEqual(cat.run(), f'{cat.name} is running')
        
if __name__ == '__main__':
    unittest.main(verbosity=2)