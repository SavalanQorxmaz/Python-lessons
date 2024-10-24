# class Animal:

# import random, os, time

# class Person:
#     def __init__(self, name, gender, is_driver, attack_damage):
#         self.name = name
#         self.gender = gender
#         self.is_driver = is_driver
#         self.attack_damage = attack_damage
#         self.hp = 100

# initialize

# leyla = Person("Leyla", "F", False, 20)
# john = Person("John", "M", True, 25)

# while True:
#     time.sleep(0.5)
#     os.system("clear")
#     print(f"{leyla.hp}\n{john.hp}")
#     leyla.hp -= john.attack_damage
#     john.hp -= leyla.attack_damage

#     if john.hp <= 0 or leyla.hp <= 0:
#         print("John is winner")
#         break