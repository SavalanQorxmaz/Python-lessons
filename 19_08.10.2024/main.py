import random

# user_input = input('Your email: ')
# def mail_generator(email: str):
#     if email.find('@') != -1:
#         return email
#     else:
#         return email + '@gmail.com'
# correct_email = mail_generator(user_input)
# print(correct_email)

# longtitude = 40
# latitude = 49

# def map_link_generator(lo, la):
#     return f'https://www.google.com/maps/@{lo},{la}'

# link = map_link_generator(longtitude, latitude)
# print(link)

operators = {
    'azercell': '50',
    'bakcell': '55',
    'nar': '70'
}

# user_operator = input('Nomreni daxil et: ')

def number_generator(operator:str):
    number = operators[operator]
    for _ in range(7):
        num = random.randrange(0, 9)
        number += (str(num))

    return number
    
number = number_generator('bakcell')
print(number)
