import random
import logging
import sys
# print(sys.getrecursionlimit())
# sys.setrecursionlimit(1500)
# print(sys.getrecursionlimit())
logging.basicConfig(
    level=logging.DEBUG, 
    filename="py_log.log",
    filemode="a",
    format="%(asctime)s %(levelname)s %(message)s"
    )

logger = logging.getLogger(__name__)
logger.level = 0
handler = logging.FileHandler('test.log', mode='w')
formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s  %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.info('logger info')

# logging.debug("A DEBUG Message")
# logging.info("An INFO")
# logging.warning("A WARNING")
# logging.error("An ERROR")
# logging.critical("A message of CRITICAL severity")

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

# operators = {
#     'azercell': '50',
#     'bakcell': '55',
#     'nar': '70'
# }

# # user_operator = input('Nomreni daxil et: ')

# def number_generator(operator:str):
#     number = operators[operator]
#     for _ in range(7):
#         num = random.randrange(0, 9)
#         number += (str(num))

#     return number
    
# number = number_generator('bakcell')
# print(number)
# logging.info(f'Log info')
# try:
#     user_input = int(input('Reqem daxil et: '))
#     # print(user_input)
#     logging.debug(f'{user_input}')
# except ValueError as err:
#     logging.error(f'{err}')
