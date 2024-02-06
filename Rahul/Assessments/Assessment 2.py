# # Q1
# def Phone_no(func):
#     def abc(numbers):
#         codes = ["+91" + number[-10:] for number in numbers]
#         return func(sorted(codes))
#     return abc
# @Phone_no
# def sorted_no(nos):
#     for n in nos:
#         Correct = f"{n[:3]} {n[3:8]} {n[8:]} "
#         print(Correct)
#
#
# n = int(input("Enter number of Phone Nos.: "))
#
# print("Print the phone numbers: ")
# nos = [input() for i in range(n)]
#
# print("Sorted Phone List: ")
# sorted_no(nos)





# # Q2
from datetime import datetime
class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        # self.age=self.createEmp(name,date)

    def __str__(self):
        return f"Name is {self.name}\nAge is {self.age}"

    @classmethod
    def createEmp(cls,name,age):
        today_date=datetime.today()
        year=datetime.strptime(age,"%d/%m/%Y")
        # today=datetime.now()

        age=today_date.year-year.year-((today_date.month,today_date.day)<(year.month, year.day))

        return cls(name,age)

# Employee.createEmp(name="kennedy", date= "23/04/1990")
emp1=Employee.createEmp("Kennedy","24/04/1990")

print(emp1)






# # Q3
# class Cart:
#     def __init__(self):
#         self.items = {}
#
#     def add_item(self, item, price, quan=1):
#         if item in self.items:
#
#             self.items[item]['quan'] += quan
#         else:
#
#             self.items[item] = {'price': price, 'quan': quan}
#
#         print(f"Added {quan} {item}(s) to the cart.")
#
#     def remove_item(self, item, quan=1):
#         if item in self.items:
#             if quan >= self.items[item]['quan']:
#                 del self.items[item]
#             else:
#
#                 self.items[item]['quan'] -= quan
#             print(f"Removed {quan} {item}(s) from the cart.")
#         else:
#             print(f"{item} not found in the cart.")
#
#     def calculate_total_price(self):
#         total_price = sum(item['price'] * item['quan'] for item in self.items.values())
#         return total_price
#
#     def display_cart(self):
#         print("\nItems in Cart:")
#         for item, details in self.items.items():
#             print(f"{item}: Rs.{details['price']} x {details['quan']}")
#
#
# cart = Cart()
#
# cart.add_item("Monitor", 2000)
# cart.add_item("CPU", 6000, 2)
# cart.add_item("Mouse", 30)
#
# cart.display_cart()
#
# cart.remove_item("CPU", 1)
#
# cart.display_cart()
#
# total_price = cart.calculate_total_price()
# print(f"\nTotal Price: Rs.{total_price}")
