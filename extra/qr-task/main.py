
# import qrcode


# import io
# import qrcode
# qr = qrcode.QRCode()
# qr.add_data("Some text")
# f = io.StringIO()
# qr.print_ascii(out=f)
# f.seek(0)
# print(f.read())

import qrcode
qr = qrcode.QRCode()
qr.add_data('Some data')
img = qr.make_image()
img.show()
qr.clear()
qr.add_data('New data')
other_img = qr.make_image()
other_img.show()