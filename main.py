class Cart():
    def __init__(self):
        self.goods = []

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        del self.goods[indx]

    def get_list(self):
        return [f'{el.name}: {el.price}' for el in self.goods]

class Table():
    def __init__(self, name, price):
        self.name = name
        self.price = price


class TV():
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Notebook():
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cup():
    def __init__(self, name, price):
        self.name = name
        self.price = price


cart = Cart()
cart.add(TV('Samsung', 1700))
cart.add(TV('Philips', 1500))
cart.add(Table('AMI', 300))
cart.add(Notebook('Lenovo', 1700))
cart.add(Cup('AMI', 10))

