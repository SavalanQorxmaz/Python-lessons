
from datetime import date

# print(date.today())

class Person:
    def __init__(self, name:str, birth_year: int) -> None:
        self.name = name
        self.birth_year = birth_year
        
    def get_birth_year(self):
        print(self.birth_year)
        return self.birth_year
    
    @staticmethod
    def get_today():
        print(date.today())
        return date.today()
    
    @classmethod
    def new_object(cls, name, birth_year):
        return cls(name, birth_year)
    @property
    def get_age(self):
        age = date.today().year - self.birth_year
        print(age)
        return age
    
    
nigar = Person('Nigar', 1995)
nigar.get_birth_year()
nigar.get_today()
Person.get_today()
nigar2 = Person.new_object('Nigar2', 1996)
nigar2.get_age
