import random

PRICE_DOSTOYEVSKI_CINAYETVECEZA = 3
PRICE_SARTR_VARLIQVEHECLIK = 5
PRICE_KAMUS_YAD = 9
PRICE_CAVID_IBLIS = 8
PRICE_NIZAMI_XAMSA = 7

book_amount = {
    'dostoyevski': PRICE_DOSTOYEVSKI_CINAYETVECEZA,
    'sartr': PRICE_SARTR_VARLIQVEHECLIK,
    'kamus': PRICE_KAMUS_YAD,
    'cavid': PRICE_CAVID_IBLIS,
    'nizami': PRICE_NIZAMI_XAMSA,
}

stock = {
    'dostoyevski': 50,
    'sartr': 35,
    'kamus': 27,
    'cavid': 42,
    'nizami': 30,
}

shopping_list = {}

balance = random.randrange(100, 301, 50)
print(balance)

finish = False
while not finish:
    selected_book = input('Enter book: ').strip().lower()
    has_book = selected_book in stock
    if not has_book:
        print('Not any')
        pass
    else:
        count_str = input('Enter count: ')
        count = 0
        is_count_integer = False
        while not is_count_integer:  # Check if input is number
            try:
                if int(count_str):
                    count = int(count_str)
                    is_count_integer = True
            except ValueError:
                print('Only number!')
                count_str = input('Number: ')
                pass
        if count > stock[selected_book]:
            print('Not enough book')
            pass
        else:
            sum = count * stock[selected_book]
            if balance < sum:
                print(f'Not enough balance, Your balance: {balance}')
                pass
            else:
                balance -= sum
                stock.update({selected_book: stock[selected_book] - count})
                shopping_list.update({selected_book: shopping_list.get(selected_book, 0) + count})
                print(f'You bought {count} {selected_book} and paid {sum}. Your current balance is {balance}')
    print(f'Your shopping list: {shopping_list}')          
    stop = input('If you want finish shopping, write - (dash): ')
    if stop.strip() == '-':
        finish = True