import re
import string
import logging

logging.basicConfig(
    level= logging.NOTSET,
    format='%(asctime)s %(levelname)s %(message)s'
)
info = logging.info
error = logging.error
    
# alpha_rangoli matrisini hazirlayan funksiya
def f_alpha_rangoli(letters: list, matrix: list = []) -> list:
    if len(matrix) == 0:
        matrix.append(letters[1:][::-1] + letters)
        letters.pop(0)
    else:
        matrix.append(letters[1:][::-1] + letters)
        matrix.insert(0, letters[1:][::-1] + letters)
        letters.pop(0)
    if len(letters) == 0:
        return matrix
    return f_alpha_rangoli(letters, matrix= matrix)

# matrise - elave etmek ucun funksiya, f_alpha_rangoli rekursiv oldugu ucun dekoratorla yaza bilmedim
def df_add_defis(matrix):
        if len(matrix):
            result = ''
            length = len(matrix) 
            full_length = 2 * length - 1
            for i in range(length):
                rest = (full_length - (len(matrix[i]) * 2 - 1)) // 2
                result += f'\n{'-' * rest + '-'.join(matrix[i]) + '-' * rest}'
        return result



# Proqrami sonlandirma ucun
stop = False
while not stop:
    # Istifadeciden nomre alinmasi, interval xarici eded yaxud diger simvollarda tekrarlanma
    correct = False
    while not correct:
        try:
            number = int(input('1-27 arasi eded daxil et, cixmaq ucun 0: '))
            if 0 < number < 27:
                letters = re.findall(r'\w', string.ascii_letters[:number])
                matrix = f_alpha_rangoli(letters, matrix = [])
                result = df_add_defis(matrix)
                info(result)
                result = ''
                correct = True
            elif number == 0:
                    correct = True
                    stop = True
            else:
                print('Yanlis Interval')
        except ValueError:
                print('Yanlis format')
        

