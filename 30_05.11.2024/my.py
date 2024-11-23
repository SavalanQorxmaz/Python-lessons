
class Animal:
    def __init__(self):
        pass
    
    def sleep():
        print('Sleeping')


class Duck(Animal):
    pass


class Lion(Animal):
    pass

class Porsuq(Animal):
    pass

Duck.sleep()


lst = [1, 2, 3, 4, 5]

current_index = 2
print(f'{current_index=}')
positions = ['1', '-1', '+2']
while True:
    position = input('position: ')
    if position == '1':
        if current_index == len(position) - 1:
            current_index  = 0
        else:
            current_index +=1
    elif position == '-1':
        lst = lst[::-1]
        current_index = len(lst) - current_index
    elif position == '+2':
        current_index  = (current_index + 2) % (len(lst)-1)
    lst = lst[current_index+1:] + lst[:current_index+1]
    print(lst)