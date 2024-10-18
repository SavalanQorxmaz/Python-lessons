'''
Kitabxana Kataloq Sistemi :  İstifadəçilərin öz kitabları ilə kitab əlavə edə biləcəyi kitabxana kataloqu sistemi yaradınbaşlıqlar və müəlliflər, 
kitabları silin, kitabları başlıq və ya müəllifə görə axtarın və siyahısını göstərinmövcud kitablar. Kitab adlarını və müəllifləri saxlamaq üçün 
lüğətdən istifadə edin və for looplarından, while, function, istifadə edin kataloq əməliyyatlarının həyata keçirilməsi.
'''




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
        books.write(f'{[*map(lambda key, value: f'{key}: {value}', book.keys(), book.values())]}\n')  
# f_add_book()


def f_read_books():
    with open('books.txt', mode='r') as books:
        line = books.readlines()
        return line



print(f'Yeni kitab daxil etmek ucun 1,\tAxtaris ucun 2,\tSilmek ucun 3')
request = input('1, 2, 3: ')
try:
    if request == '1':
        print('Yeni kitab...')
        f_add_book()
        books = f_read_books()
        print(books)
    elif request == '2':
        print('Axtaris...')
        pass
    elif request == '3':
        print('Silmek...')
        pass
    else:
        print('Yanlis secim')
except:
    'Xeta'


