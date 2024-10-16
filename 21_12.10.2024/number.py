
import logging
import re

logging.basicConfig(
    level=logging.NOTSET,
    format="%(asctime)s %(levelname)s %(message)s"
)
info = logging.info
error = logging.error

def f_check_operator(prefix: int) -> str:
    operators = {
        'azercell': [50, 51, 10],
        'bakcell': [55, 99],
        'nar': [70, 77]
    }
    filtered = []
    for key in operators:
        filtered = [*filter(lambda x: x == prefix, operators[key])]
        if filtered:
            return key.title()
    return False

def f_check_number(number: str):
    check_number_format = re.search('(^\+994)(10|50|51|55|70|77)([2-9][0-9][0-9][0-9][0-9][0-9][0-9]$)', number)
    operator = ''
    print(check_number_format)


    if check_number_format:
        operator = f_check_operator(int(number[4:6]))
        if operator:
            info(f'operator: {number[4:6]}({operator}), number: {number[-7:]}')
        else:
            error('Unknown operator')
    else:
        error('Incorrect format')
    
    
number = input('Nomreni daxil et: ')
f_check_number(number)