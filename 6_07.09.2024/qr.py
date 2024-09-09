import qrcode
import requests
import webbrowser

# data = 'QR Code using make() function'
 
# # Encoding data using make() function
# img = qrcode.make(data)
 
# # Saving as an image file
# img.save('MyQRCode1.png')

img1 = qrcode.make('Some data here')
print(type(img1))  # qrcode.image.pil.PilImage
# img.save("some_file.png")

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('Some data')
qr.make(fit=True)

img = qr.make_image(fill_color="white", back_color="red")
img.save('colored.png')

r = requests.get('https://www.youtube.com/watch?v=Gl7BXCbqPIs')
print(r.text)

url = 'https://www.youtube.com/watch?v=Gl7BXCbqPIs'
webbrowser.open(url)