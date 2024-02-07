


class Product:

    def __init__(self, price):
        self.__price = price        # private variable

    @property
    def price(self):
        print("getter called...")
        return f"price is rs.{self.__price}"

    @price.setter
    def price(self, prc):
        print("setter called.....")
        self.__price = prc

    @price.deleter
    def price(self):
        print("deleter called.....")
        self.__price = 0


coke = Product(60)
print(coke.price)

coke.price = 120
print(coke.price)

del coke.price
print(coke.price)

