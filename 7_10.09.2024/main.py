surname = input('Your Surname: ')
if len(surname) > 6:
    print(f'Your surname is: {surname}')

list1 = [4, 7, 73, 8, 98, 20]
list1.sort()
list2 = list1[3:]
print(list1)
orta_eded = sum(list2) / 3
print(orta_eded)