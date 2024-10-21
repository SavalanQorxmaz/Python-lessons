from math import sqrt

def is_prime(number):
    if not isinstance(number, int):
        raise TypeError(
            f"integer number expected, got {type(number).__name__}"
        )
    if number < 2:
        raise ValueError(f"integer above 1 expected, got {number}")
    for candidate in range(2, int(sqrt(number)) + 1):
        if number % candidate == 0:
            return False
    return True

print(is_prime(3))


def is_number(number: str):
    try:
        if not number.isdigit():
            pass
        print(int(number))
        raise TypeError(f'Parameter is {type(number).__name__}')
    except:
        raise

is_number('2')