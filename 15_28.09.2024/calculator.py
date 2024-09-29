

operators = (('^',), ('*', '/'), ('+', '%'))
all_operators = []
for oper in operators:
    all_operators.extend(oper)
print(all_operators)
print_operators = tuple(x if x != '^' else '**' for x in all_operators)
print_operators = tuple(x if x != '%' else '-' for x in print_operators)
print(f'Operators: {print_operators}')
user_input = input('mathematical expression:  ')
while len(user_input) == 0:
    user_input = input('mathematical expression required:  ')
print(user_input)
# lst = user_input.split() 

# Ifadenin simvollar massivine cevrilmesi (bosluq xaric)
lst = [x for x in user_input if x != ' ']

# Cox reqemli edelerin reqemlerinin birlesdirilmesi, ** ifadesinin ^ ile(Teklesdirilme),
# - ifadesinin % ile evezlenmesi(Netice - olduqda problem yaranir) evezlenmesi: 
i = 0
while i < len(lst)-1:
    if (lst[i].isdigit() or lst[i].endswith('.')) and  (lst[i+1].isdigit() or lst[i+1] == '.'):
        lst[i:i+2] = [lst[i] + lst[i+1]]
        i -= 1
    elif (lst[i] ==  lst[i+1] == '*'):
        lst[i:i+2] = ['^']
        i -= 1
    elif (lst[i]  == '-'):
        lst[i:i+1] = ['%']
    i += 1
# print(lst)

# Reqemlerin int tipine cevrilmesi, kenar simvol oluqda proqramin sonlanmasi
lst = [int(x) if x.isdigit() else x for x in lst ]

for x in lst:
    if ((not type(x) is int) and (not x in all_operators)):
        exit(f'Incorrect input: {x}')

# Hesablama
for operators_group in operators:
    ready = False
    while not ready:
        lst_str = ''.join(str(x) for x in lst)
        for operator in lst_str:
            if operator in operators_group:
                index = lst.index(operator)
                if operator == '^':
                    lst[index-1:index+2] = [lst[index-1] ** lst[index +1]]
                    break
                elif operator == '*':
                    lst[index-1:index+2] = [lst[index-1] * lst[index +1]]
                    break
                elif operator == '/':
                    lst[index-1:index+2] = [lst[index-1] / lst[index +1]]
                    break
                elif operator == '+':
                    lst[index-1:index+2] = [lst[index-1] + lst[index +1]]
                    break
                elif operator == '%':
                    lst[index-1:index+2] = [lst[index-1] - lst[index +1]]
                    break
                
        else:
            ready = True
print(lst)