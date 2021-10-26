class Product:
    def __init__(self, name, price, size):
        self.name = name
        self.price = price
        self.size = size
    def __str__(self):
        return f'name-{self.name}, price-{self.price}, size-{self.size}'


prod_1 = Product('phone', 100, 'S')
prod_2 = Product('tv', 250, 'M')
print(prod_1)
print(prod_2)


class Buyer:
    def __init__(self, name, surname, phone):
        self.name = name
        self.surname = surname
        self.phone = phone
    def __str__(self):
        return f'Buyer: {self.name} {self.surname}, phone number- {self.phone}'

buyer_1 = Buyer('ivan', 'Ivanov', 12345)
buyer_2 = Buyer('Petr', 'Petrov', 54321)
print(buyer_1)
print(buyer_2)


class Order:
    def __init__(self, name, surname, *args):
        self.args = args
        self.surname = surname
        self.name = name
    def __str__(self):
        return f'name - {self.name} {self.surname}, order: {self.args}'
    def sum_order(self):
        pass



order_1 = Order('Ivan', 'Ivanov', 'phone', 'tv', 'laptop')
print(order_1)