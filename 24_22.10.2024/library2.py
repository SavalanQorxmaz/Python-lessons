import re
import unittest
    
    
class Book:
    def __init__(self, name, writer, pages, count) -> None:
        self.name = name
        self.writer = writer
        self.pages = pages
        self.count = count
        
    def __str__(self) -> str:
        return f'{self.name}:{self.writer}:{self.pages}:{self.count}'
    


# Yeni kitab obyekti yaratmaq ucun funksiya
def f_new_book():
    """
    Istifadeciden alinan kitab informasiyasinin duzgunluyunu yoxlamaq ve uygun formada 
    qaytarmaq ucun funksiya
    """
    print('Bazaya daxil etmek ucun kitab haqda informasiyani daxil et')
    writer = input('Yazici: ')
    book = input('Kitab: ')
    correct_pages = False
    while not correct_pages:
        try:
            pages = int(input('Sehife sayi: '))
            correct_pages = True
        except ValueError:
            print('Sehife sayi formatini duz daxil et: ')
    correct_count = False
    while not correct_count:
        try:
            count = int(input('Kitab sayi: '))
            correct_count = True
        except ValueError:
            print('Kitab sayi formatini duz daxil et: ')
    return Book(writer, book, pages, count)

# istifadecinin secimini mueyyen etmek ucun funksiya
def f_selected_step():
    print('Variantlardan birini sec:')
    message = '''
          -Siyahiya baxmaq ucun:     1
          -Kitab elave etmek ucun:   2
          -Kitab redakte etmek ucun: 3
          -Kitab silmek ucun:        4
          '''
    print(message)
    variant = input('Secim: ')
    while variant not in('1234'):
        print('Daxil etdiyiniz variant movcud deyil')
        print(message)
        variant = input('Secim: ')
    else:
        return variant
    

# Fayldan siyahiyini elde etmek ucun funksiya
def f_get_all_books():
    with open('books.txt', mode='r') as all_books:
        objs = []
        lines = all_books.readlines()
    for i,line in enumerate(lines):
            line = line.split('\n')[0]
            line = line.split(':')
            # lines[i] = dict((x.split(':')[0],x.split(':')[1]) for x in line )
            obj = Book(writer=line[0], name=line[1], pages=int(line[2]), count=line[3])
            objs.append(obj)
    if len(objs)== 0:
        return None
    else:
        return objs

# Kitablari gostermek funksiyasi
def f_show_books(objs):
    if not objs:
        print('Siyahi bosdu')
    else:
        for i, obj in enumerate(objs, start=1): 
            print(f'{i}: {obj}')

# Kitab secmek ucun funksiya( hem silmek, hem redakte ucun istifade olunacag) index qaytaracaq

def f_get_book_index(objs):
        f_show_books(objs)
        correct_choose = False
        while not correct_choose:
            print('Imtina ucun 0 daxil et')
            try:
                index =  int(input('Redakte etmek istediyin kitabin indeksini sec: '))
                if index == 0:
                   return 0
                elif index in set(range(1, len(objs)+1)):
                    correct_choose = True
                    return index
                else:
                    print('Indeks movcud deyil')
                
            except ValueError:
               print('Indeks xetasi')
               
# Siyahidan  kitab silmek ucun funksiya
def f_delete_book(index, objs): 
    objs.pop(index-1)
    f_show_books(objs)
    if objs:
        objs = '\n'.join([x.__str__() for x in objs]) + '\n'
    else:
        objs = ''
    with open('books.txt','w') as books:
        books.write(objs)

# Axtarish funksiyasi
def f_search(data):
    objs = f_get_all_books()
    # objs =  [obj.__str__() for obj in objs]
    for obj in objs:
        obj = obj.__str__()
        search = re.search(data, obj)
        if search:
            span = search.span()
            print(f'{obj[:span[0]]}{'\033[91m' + data + '\033[0m'}{obj[span[1]:]}')


# Prosesi idare etmek ucun funksiya
def f_process():
    objs = f_get_all_books()
    step = f_selected_step()
    if step == '1':
        f_show_books(objs)
    elif step == '2':
        new_book = f_new_book().__str__()
        with open('books.txt','a') as books:
            books.write(new_book + '\n')
            print('Kitab elave edildi')
    elif step == '3':
        data = input('Axtaris sozunu daxil et: ')
        f_search(data)
            
    elif step == '4':
        if not objs:
            print('Siyahi bosdu')
        else:
            index = f_get_book_index(objs)
            if index == -1:
                print('Indeks movcud deyil')
            elif index == 0:
                print('Proses dayandirildi')
            else:
                f_delete_book(index, objs)

    
    
class TestLibrary(unittest.TestCase):
    def test_select_step(self):
        pass
        

if __name__ == '__main__':          
    f_process()
    # unittest.main(verbosity=2)