class Account:
    def __init__(self, amt, name):

        self.amt = amt
        self.name = name
        self.res = []

    def __str__(self):
        return f"Account Holder Name: {self.name}, Balance: {self.amt}"



    def Deposit(self, amt):
        self.amt += amt

    def Withdrawal(self, amt):
        self.amt -= amt

    def __gt__(self, other):
        return self.amt > other.amt

    def __ge__(self, other):
        return self.amt >= other.amt


    def __eq__(self, other):
        return self.amt == other.amt

    def AddNominee(self, nominee):
        self.res.append(nominee)


    def __len__(self):
        return len(self.res)

    def __iter__(self):
        return iter(self.res)
#
#
#
#
#
#
#
#
# class Account:
#     def __init__(self, balance, holder):
#         self.balance = balance
#         self.holder = holder
#         self.nominees = []
#
#     def Deposit(self, amount):
#         self.balance += amount
#
#     def Withdrawal(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#         else:
#             print("Insufficient funds")
#
#     def AddNominee(self, nominee):
#         self.nominees.append(nominee)
#
#     def __str__(self):
#         return f"Account Holder: {self.holder}, Balance: {self.balance}"
#
#     def __eq__(self, other):
#         return self.balance == other.balance
#
#     def __ne__(self, other):
#         return self.balance != other.balance
#
#     def __gt__(self, other):
#         return self.balance > other.balance
#
#     def __lt__(self, other):
#         return self.balance < other.balance
#
#     def __ge__(self, other):
#         return self.balance >= other.balance
#
#     def __le__(self, other):
#         return self.balance <= other.balance
#
#     def __len__(self):
#         return len(self.nominees)
#
#     def __iter__(self):
#         return iter(self.nominees)
