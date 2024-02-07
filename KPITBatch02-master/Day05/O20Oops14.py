

class Product:

    def __init__(self, price):
        self.__price = price        # private variable

    def getprice(self):
        print("getter called...")
        return f"price is rs.{self.__price}"

    def setprice(self, prc):
        print("setter called.....")
        self.__price = prc

    def deleteprice(self):
        print("deleter called.....")
        self.__price = 0


    price = property(getprice, setprice, deleteprice)

coke = Product(60)
print(coke.price)

coke.price = 120
print(coke.price)

del coke.price
print(coke.price)
