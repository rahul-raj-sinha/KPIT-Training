
class Product:

    def __init__(self, price):
        self.__price = price        # private variable

    def getprice(self):
        return f"price is rs.{self.__price}"

    def setprice(self, prc):
        if prc < 0:
            raise ValueError("Price cannot be less than zero....")
        else:
            self.__price = prc

    def deleteprice(self):
        self.__price = 0

import sys

try:
    pepsi = Product(50)
    print(pepsi.getprice())
    pepsi.setprice(75)
    print(pepsi.getprice())

    pepsi.deleteprice()
    print(pepsi.getprice())

except:
    print("Exception raised.....")
    print(sys.exc_info()[0])
    print(sys.exc_info()[1])
