# # Linked List

# class Node:
#     def __init__(self, data=None, next=None):
#         self.data = data
#         self.next = next


# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def print(self):
#         if self.head is None:
#             print("Linked list is empty")
#             return
#         itr = self.head
#         llstr = ''
#         while itr:
#             llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
#             itr = itr.next
#         print(llstr)

#     def get_length(self):
#         count = 0
#         itr = self.head
#         while itr:
#             count += 1
#             itr = itr.next

#         return count

#     def insert_at_begining(self, data):
#         node = Node(data, self.head)
#         self.head = node

#     def insert_at_end(self, data):
#         if self.head is None:
#             self.head = Node(data, None)
#             return

#         itr = self.head

#         while itr.next:
#             itr = itr.next

#         itr.next = Node(data, None)

#     def insert_at(self, index, data):
#         if index < 0 or index > self.get_length():
#             raise Exception("Invalid Index")

#         if index == 0:
#             self.insert_at_begining(data)
#             return

#         count = 0
#         itr = self.head
#         while itr:
#             if count == index - 1:
#                 node = Node(data, itr.next)
#                 itr.next = node
#                 break

#             itr = itr.next
#             count += 1

#     def remove_at(self, index):
#         if index < 0 or index >= self.get_length():
#             raise Exception("Invalid Index")

#         if index == 0:
#             self.head = self.head.next
#             return

#         count = 0
#         itr = self.head
#         while itr:
#             if count == index - 1:
#                 itr.next = itr.next.next
#                 break

#             itr = itr.next
#             count += 1

#     def insert_values(self, data_list):
#         self.head = None
#         for data in data_list:
#             self.insert_at_end(data)

#     def insert_after_value(self, data_after, data_to_insert):
#         # Search for first occurance of data_after value in linked list
#         # Now insert data_to_insert after data_after node
#         pass

#     def remove_by_value(self, data):
#         # Remove first node that contains data
#         pass


# if __name__ == '__main__':
#     ll = LinkedList()
#     # data_list = input

#     data = input().split(",")
#     ll.insert_values(data)
#     ll.insert_at_end(67)
#     ll.remove_at(2)
#     ll.print()






# # Double Linked List

# class Node:
#     def __init__(self, data=None, prev=None, next=None):
#         self.data = data
#         self.prev = prev
#         self.next = next


# class DoublyLinkedList:
#     def __init__(self):
#         self.head = None

#     def print_forward(self):
#         if self.head is None:
#             print("Doubly linked list is empty")
#             return
#         itr = self.head
#         llstr = ''
#         while itr:
#             llstr += str(itr.data) + ' --> ' if itr.next else str(itr.data)
#             itr = itr.next
#         print("Forward:", llstr)

#     def print_backward(self):
#         if self.head is None:
#             print("Doubly linked list is empty")
#             return
#         # Move itr to the last node
#         itr = self.head
#         while itr.next:
#             itr = itr.next
#         llstr = ''
#         while itr:
#             llstr += str(itr.data) + ' --> ' if itr.prev else str(itr.data)
#             itr = itr.prev
#         print("Backward:", llstr)

#     def get_length(self):
#         count = 0
#         itr = self.head
#         while itr:
#             count += 1
#             itr = itr.next
#         return count

#     def insert_at_beginning(self, data):
#         if self.head is None:
#             self.head = Node(data)
#         else:
#             node = Node(data, None, self.head)
#             self.head.prev = node
#             self.head = node

#     def insert_at_end(self, data):
#         if self.head is None:
#             self.head = Node(data)
#             return
#         itr = self.head
#         while itr.next:
#             itr = itr.next
#         itr.next = Node(data, itr)

#     def insert_at(self, index, data):
#         if index < 0 or index > self.get_length():
#             raise Exception("Invalid Index")

#         if index == 0:
#             self.insert_at_beginning(data)
#             return

#         count = 0
#         itr = self.head
#         while itr:
#             if count == index - 1:
#                 node = Node(data, itr, itr.next)
#                 if itr.next:
#                     itr.next.prev = node
#                 itr.next = node
#                 break
#             itr = itr.next
#             count += 1

#     def insert_after_value(self, data_after, data_to_insert):
#         if self.head is None:
#             return

#         itr = self.head
#         while itr:
#             if itr.data == data_after:
#                 node = Node(data_to_insert, itr, itr.next)
#                 if itr.next:
#                     itr.next.prev = node
#                 itr.next = node
#                 break
#             itr = itr.next

#     def remove_by_value(self, data):
#         if self.head is None:
#             return

#         if self.head.data == data:
#             self.head = self.head.next
#             if self.head:
#                 self.head.prev = None
#             return

#         itr = self.head
#         while itr:
#             if itr.data == data:
#                 itr.prev.next = itr.next
#                 if itr.next:
#                     itr.next.prev = itr.prev
#                 break
#             itr = itr.next


# if __name__ == '__main__':
#     dll = DoublyLinkedList()

#     data_list = input("Enter data elements for doubly linked list (comma separated): ").split(",")
#     for data in data_list:
#         dll.insert_at_end(data)

#     dll.print_forward()
#     dll.print_backward()

#     data_after = input("Enter the data after which you want to insert: ")
#     data_to_insert = input("Enter the data to insert: ")
#     dll.insert_after_value(data_after, data_to_insert)
#     dll.print_forward()
#     dll.print_backward()

#     data_to_remove = input("Enter the data to remove: ")
#     dll.remove_by_value(data_to_remove)
#     dll.print_forward()
#     dll.print_backward()






# # Circular Linked List

# class Node:
#     def __init__(self, data=None):
#         self.data = data
#         self.next = None


# class CircularLinkedList:
#     def __init__(self):
#         self.head = None

#     def print_list(self):
#         if self.head is None:
#             print("Circular linked list is empty")
#             return
#         itr = self.head
#         llstr = ''
#         while True:
#             llstr += str(itr.data) + ' --> '
#             itr = itr.next
#             if itr == self.head:
#                 break
#         print(llstr)

#     def get_length(self):
#         count = 0
#         itr = self.head
#         if itr is None:
#             return 0
#         while True:
#             count += 1
#             itr = itr.next
#             if itr == self.head:
#                 break
#         return count

#     def insert_at_beginning(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             new_node.next = new_node
#             self.head = new_node
#             return
#         itr = self.head
#         while itr.next != self.head:
#             itr = itr.next
#         itr.next = new_node
#         new_node.next = self.head
#         self.head = new_node

#     def insert_at_end(self, data):
#         if self.head is None:
#             self.insert_at_beginning(data)
#             return
#         new_node = Node(data)
#         itr = self.head
#         while itr.next != self.head:
#             itr = itr.next
#         itr.next = new_node
#         new_node.next = self.head

#     def insert_at(self, index, data):
#         if index < 0 or index > self.get_length():
#             raise Exception("Invalid Index")

#         if index == 0:
#             self.insert_at_beginning(data)
#             return

#         count = 0
#         itr = self.head
#         while True:
#             if count == index - 1:
#                 new_node = Node(data)
#                 new_node.next = itr.next
#                 itr.next = new_node
#                 break
#             itr = itr.next
#             count += 1
#             if itr.next == self.head:
#                 break

#     def insert_after_value(self, data_after, data_to_insert):
#         if self.head is None:
#             return
#         itr = self.head
#         while True:
#             if itr.data == data_after:
#                 new_node = Node(data_to_insert)
#                 new_node.next = itr.next
#                 itr.next = new_node
#                 break
#             itr = itr.next
#             if itr == self.head:
#                 break

#     def remove_by_value(self, data):
#         if self.head is None:
#             return
#         if self.head.data == data:
#             itr = self.head
#             while itr.next != self.head:
#                 itr = itr.next
#             itr.next = self.head.next
#             self.head = self.head.next
#             return

#         itr = self.head
#         while True:
#             if itr.next.data == data:
#                 itr.next = itr.next.next
#                 break
#             itr = itr.next
#             if itr == self.head:
#                 break


# if __name__ == '__main__':
#     cll = CircularLinkedList()

#     data_list = input("Enter data elements for circular linked list (comma separated): ").split(",")
#     for data in data_list:
#         cll.insert_at_end(data)

#     cll.print_list()

#     data_after = input("Enter the data after which you want to insert: ")
#     data_to_insert = input("Enter the data to insert: ")
#     cll.insert_after_value(data_after, data_to_insert)
#     cll.print_list()

#     data_to_remove = input("Enter the data to remove: ")
#     cll.remove_by_value(data_to_remove)
#     cll.print_list()





