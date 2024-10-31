import datetime

class Product:
    def __init__(self, name, price, date=(2024, 10, 1)):
        self.name = name
        self.price = price
        self.date = datetime.datetime(*date)  + datetime.timedelta(30) - datetime.datetime.now() 
    def __repr__(self):
        return f'{(self.name, self.price, f'{self.date.days} days')}'

class User:
    def __init__(self, nickname):
        self.nickname = nickname
        self.basket = []
        

    def buy_product(self, product):
        self.basket.append(product)

    def __str__(self):
        return f'{self.nickname} : {self.basket}'
    
xiyar = Product('xiyar', 5, (2024, 10,1))
pomidor = Product('pomidor', 10)
kartof = Product('kartof', 3)

user = User('Filankes')
for product in(xiyar, pomidor, kartof):
    user.buy_product(product)
print(user)

