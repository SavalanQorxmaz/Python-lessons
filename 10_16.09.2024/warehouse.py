import random
warehouse_stock = {
    'sock': 46,
    'cap': 13,
    't-shirt': 52
}
stock_unit_amount = {
    'sock': 3,
    'cap': 15,
    't-shirt': 20
}

balance = random.randrange(100, 300, 50)
print(balance)
sum = 0

for i in range(2):
    clothe = input('Clothe: ').lower()
    count = int(input('Count: '))
    if clothe in warehouse_stock:
        if count <= warehouse_stock[clothe]:
            sum += stock_unit_amount[clothe] * count
            if balance < sum:
                print('Low balance')
            else:
                balance -= sum
            print(f' You buy {count} {clothe}, Sum {sum}')
        else:
            print('Not enough clothe')
    else:
        print(f'There are no {clothe} in stock')
    print(f'Your balance: {balance}')
