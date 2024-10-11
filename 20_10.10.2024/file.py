# import time

# def print_stars(func):
#     def inner(*args):
#         print("*" * 10)
#         func(*args)
#         print("*" * 10)
#     return inner

# def pause(func):
#     def wrapper(*args):
#         print("=" * 10)
#         func(*args)
#         print("=" * 10)
#     return wrapper

# @pause
# @print_stars
# def greet(name: str):
#     print(f"Hello, {name}")

# @pause
# def send_mail(address="pony@gmail.com"):
#     print("Sending mail...")

# greet("Patrick")
# # send_mail()