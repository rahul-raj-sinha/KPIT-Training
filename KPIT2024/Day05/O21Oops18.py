
from abc import ABC, abstractmethod

class Account(ABC):

    @abstractmethod
    def checkBalance(self):
        pass

    def deposit(self):
        pass



class SavingsAccount(Account):

    def fun(self):
        print("Hello World")

    def checkBalance(self):
        print("The balance in the account is #######")

save = SavingsAccount()
save.fun()
