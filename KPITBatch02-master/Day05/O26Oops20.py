
from abc import ABC, abstractmethod
class Account(ABC):

    @abstractmethod
    def getBalance(self):
        pass

    def deposit(self):
        pass


class Savings(Account):

    def getBalance(self):
        print("The balance in the account is ######")
    def fun(self):
        print("hello world")

sav = Savings()