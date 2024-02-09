
# Circular Linked List

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        if self.head is None:
            print("Circular linked list is empty")
            return
        itr = self.head
        llstr = ''
        while True:
            llstr += str(itr.data) + ' --> '
            itr = itr.next
            if itr == self.head:
                break
        print(llstr)

    def get_length(self):
        count = 0
        itr = self.head
        if itr is None:
            return 0
        while True:
            count += 1
            itr = itr.next
            if itr == self.head:
                break
        return count

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            new_node.next = new_node
            self.head = new_node
            return
        itr = self.head
        while itr.next != self.head:
            itr = itr.next
        itr.next = new_node
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        if self.head is None:
            self.insert_at_beginning(data)
            return
        new_node = Node(data)
        itr = self.head
        while itr.next != self.head:
            itr = itr.next
        itr.next = new_node
        new_node.next = self.head

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_beginning(data)
            return

        count = 0
        itr = self.head
        while True:
            if count == index - 1:
                new_node = Node(data)
                new_node.next = itr.next
                itr.next = new_node
                break
            itr = itr.next
            count += 1
            if itr.next == self.head:
                break

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return
        itr = self.head
        while True:
            if itr.data == data_after:
                new_node = Node(data_to_insert)
                new_node.next = itr.next
                itr.next = new_node
                break
            itr = itr.next
            if itr == self.head:
                break

    def remove_by_value(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            itr = self.head
            while itr.next != self.head:
                itr = itr.next
            itr.next = self.head.next
            self.head = self.head.next
            return

        itr = self.head
        while True:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next
            if itr == self.head:
                break


if __name__ == '__main__':
    cll = CircularLinkedList()

    data_list = input("Enter data elements for circular linked list (comma separated): ").split(",")
    for data in data_list:
        cll.insert_at_end(data)

    cll.print_list()

    data_after = input("Enter the data after which you want to insert: ")
    data_to_insert = input("Enter the data to insert: ")
    cll.insert_after_value(data_after, data_to_insert)
    cll.print_list()

    data_to_remove = input("Enter the data to remove: ")
    cll.remove_by_value(data_to_remove)
    cll.print_list()





