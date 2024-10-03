from random import randint

numbers = [f'Python {x}' for x in range(randint(1, 100))]

try:
    print(numbers[50])
except IndexError:
    print('Not found')
    numbers = numbers * 2
    print(numbers)