
from abc import ABC, abstractmethod

class Employee:

    @abstractmethod
    def doJob(self):
        pass

class Manager(Employee):

    def doJob(self):
        print("Manager's Job......")


class Developer(Employee):

    def doJob(self):
        print("developer's job......")

#polymorphism
def BankJob(emp):
    print("Bankjob started......")
    emp.doJob()
    print("Bankjob completed......")
    print("-" * 60)


Mike = Manager()
Jack = Developer()

BankJob(Mike)


BankJob(Jack)
