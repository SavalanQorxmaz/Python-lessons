import requests
x = requests.get('https://10.100.10.254')
print(x.text)