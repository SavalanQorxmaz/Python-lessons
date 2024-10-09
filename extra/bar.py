import barcode
from barcode.writer import ImageWriter


number = '+994558385589'

my_number = barcode.Code128(number)
my_number.save('number')

my_number = barcode.Code128(number, writer=ImageWriter())
my_number.save('number')

my_number = barcode.generate('Code128', number, writer=ImageWriter(), output='number1', text='My number')