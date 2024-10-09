import qrcode
from getpass import getpass
from PIL import Image, ImageOps
qr_size = (300, 300)
size = (90, 90)
with Image.open('wifi_logo.webp') as logo:
    logo.thumbnail(size)
    logo = ImageOps.expand(logo, border=5, fill='white').convert('RGBA')
    print(logo.mode)
    r, g, b, a = logo.split()
    # logo = Image.merge('RGB', (b, g, r))
# print(logo.size)
ssid = input('SSID: ')
print(ssid)
password = getpass('Password: ')
print(password)
security = 'WPA2'
wifi_data = 'WIFI:S:{};T:{};P:{};;'.format(ssid, security, password)

qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(wifi_data)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.thumbnail(qr_size)
print(img.size)
img_w, img_h = img.size
logo_w, logo_h = logo.size
pos = ((img_w - logo_w) // 2, (img_h - logo_h) // 2)
img.paste(logo, pos)
img.save('wifi.png')