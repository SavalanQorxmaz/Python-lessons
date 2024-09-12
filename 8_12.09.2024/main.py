import random
my_dict = {'number': 25}
# new_age  = int(input('How match: '))
new_number = random.randrange(5, 10)
my_dict['number'] += new_number
print(my_dict)