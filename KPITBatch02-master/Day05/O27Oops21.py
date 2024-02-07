
from abc import ABC, abstractmethod
class Employee(ABC):

    @abstractmethod
    def doJob(self):
        pass

class Manager(Employee):

    def doJob(self):
        print("Managers job......")

class Developer(Employee):

    def doJob(self):
        print("Develpers job......")


def BankJob(emp):
    print("Bank job started.....")
    emp.doJob()
    print("Bank job ended......")
    print("-" * 60)


mike = Manager()
david = Developer()

BankJob(mike)
BankJob(david)
