'''
Kitabxana Kataloq Sistemi :  İstifadəçilərin öz kitabları ilə kitab əlavə edə biləcəyi kitabxana kataloqu sistemi yaradınbaşlıqlar və müəlliflər, 
kitabları silin, kitabları başlıq və ya müəllifə görə axtarın və siyahısını göstərinmövcud kitablar. Kitab adlarını və müəllifləri saxlamaq üçün 
lüğətdən istifadə edin və for looplarından, while, function, istifadə edin kataloq əməliyyatlarının həyata keçirilməsi.
'''

import re

# Kitab elave etmek ucun funksiya
def f_add_book():
    book = {
    'writer': None,
    'book': None,
    'pages': None,
    'price': None
}
    for key in book:
        print(f'{key}: ')
        value = input()
        book.update({key: value})
        
    with open('books.txt', mode='a') as books:
        books.write(' '.join([*map(lambda key, value: f'{key}:{value}', book.keys(), book.values())]) + '\n')  

# Kitab siyahisini elde etmek ucun funksiya
def f_read_books():
    lines = []
    result = []
    with open('books.txt', mode='r') as books:
        lines = books.readlines()
    for i,line in enumerate(lines):
            line = line.split('\n')[0]
            line = line.split()
            lines[i] = dict((x.split(':')[0],x.split(':')[1]) for x in line )
    return lines


print(f'Yeni kitab daxil etmek ucun 1,\tAxtaris ucun 2,\tSilmek ucun 3')
request = input('1, 2, 3: ')
try:
    if request == '1':  # Yeni kitab elave etmek
        print('Yeni kitab...')
        f_add_book()
        books = f_read_books()
    elif request == '2':    # Axtaris aparmaq ucun
        print('Axtaris...')
        books = f_read_books()
        if len(books) == 0:
            print('Siyahi bosdu')
        else:
            print('Axtaris sozunu daxil et: ', end='')
            word = input()
            result = []
            for book in books:
                all_value = '-'.join([*book.values()])
                search = re.search(word, all_value)
                if search:
                    span = search.span()
                    new_line = f'{all_value[:span[0]]}{'\033[91m' + word + '\033[0m'}{all_value[span[1]:]}'
                    print(new_line)
    elif request == '3':    # Kitab silmek ucun
        print('Silmek...')
        books = f_read_books()
        books_str = ''.join([f'{i}: {book}\n' for i, book in enumerate(books)] )
        print(books_str)
        correct_indeks = False
        while not correct_indeks:
            if len(books) == 0:
                    print('Siyahi bosdu')
                    break
            try:
                print('Silmek istediyin kitabin indeksini sec: ', end='')
                indeks = int(input())
                if -1 < indeks < len(books):
                    books.pop(indeks)
                    with open('books.txt', mode='w+') as books_file:
                         print(len(books_file.readlines()))
                         books_file.write(''.join([' '.join([*map(lambda key, value: f'{key}:{value}', book.keys(), book.values())] )+ '\n' for book in books]))
                    correct_indeks = True
                else:
                    print('Indeks movcud deyil')
            except ValueError:
                print('Indeksi deqiq sec')
        pass
    else:
        print('Yanlis secim')
except:
    'Xeta'


