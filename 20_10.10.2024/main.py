# Docstring
def convert_currency(currency, amount, azn=1.7):
    """
    This function is supposed to convert
    the definite amount of money and transfer
    it ot P-Diddy
    """
    total = amount * azn
    result = total / currency
    return result

print(convert_currency.__doc__)

class Human:
    """This class is designed for human creations."""

print(Human.__doc__)