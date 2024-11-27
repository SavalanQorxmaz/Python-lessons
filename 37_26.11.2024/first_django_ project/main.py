import webbrowser
import os
import socket
import qrcode
from PIL import Image
qr = qrcode.QRCode(version=1, box_size=10, border=5)
data ='''

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <button onclick="getLocation()">Try It</button>
   <div id="demo"></div>
    
    <script>
    const x = document.getElementById("demo");

function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
  } else { 
    x.innerHTML = "Geolocation is not supported by this browser.";
  }
}

function showPosition(position) {
  x.innerHTML = "Latitude: " + position.coords.latitude + 
  "<br>Longitude: " + position.coords.longitude;
}
    </script>
</body>
</html>
'''

txt = None
with open('index.html','r') as geo:
    txt = geo.read()
    print(txt)
# qr.add_data(txt)
qr.make(txt)
img = qr.make_image(fill_color='black', back_color='white')
img.show()
    
webbrowser.open()
print(socket.gethostbyname(socket.gethostname()))

# import qrcode
# import qrcode.image.svg

# img = qrcode.make('http://127.0.0.1/')

# with open('qr.svg', 'wb') as qr:
#     img.save(qr)