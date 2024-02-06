# 1. Create a singly linked list, append items, and iterate through the list:
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next_node = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next_node:
                current_node = current_node.next_node
            current_node.next_node = new_node

    def iterate(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next_node
        print("None")


# Example usage:
singly_linked_list = SinglyLinkedList()
singly_linked_list.append(1)
singly_linked_list.append(2)
singly_linked_list.append(3)

singly_linked_list.iterate()

# 2. Find the size of a singly linked list:


def get_size(singly_linked_list):
    size = 0
    current_node = singly_linked_list.head
    while current_node:
        size += 1
        current_node = current_node.next_node
    return size


# Example usage:
size = get_size(singly_linked_list)
print("Size of the singly linked list:", size)

# 3. Search a specific item in a singly linked list:


def search_item(singly_linked_list, target):
    current_node = singly_linked_list.head
    while current_node:
        if current_node.data == target:
            return True
        current_node = current_node.next_node
    return False


# Example usage:
result = search_item(singly_linked_list, 2)
print("Item found:", result)

# 4. Access a specific item in a singly linked list using index value:


def access_item(singly_linked_list, index):
    current_node = singly_linked_list.head
    count = 0
    while current_node:
        if count == index:
            return current_node.data
        count += 1
        current_node = current_node.next_node
    return None


# Example usage:
item = access_item(singly_linked_list, 1)
print("Item at index 1:", item)

# 5. Set a new value of an item in a singly linked list using index value:


def set_value(singly_linked_list, index, new_value):
    current_node = singly_linked_list.head
    count = 0
    while current_node:
        if count == index:
            current_node.data = new_value
            return True
        count += 1
        current_node = current_node.next_node
    return False


# Example usage:
result = set_value(singly_linked_list, 1, 10)
if result:
    singly_linked_list.iterate()
else:
    print("Index out of bounds.")

# 6. Delete the first item from a singly linked list:


def delete_first_item(singly_linked_list):
    if singly_linked_list.head:
        singly_linked_list.head = singly_linked_list.head.next_node


# Example usage:
delete_first_item(singly_linked_list)
singly_linked_list.iterate()

# 7. Delete the last item from a singly linked list:


def delete_last_item(singly_linked_list):
    if not singly_linked_list.head:
        return

    if not singly_linked_list.head.next_node:
        singly_linked_list.head = None
        return

    current_node = singly_linked_list.head
    while current_node.next_node.next_node:
        current_node = current_node.next_node
    current_node.next_node = None


# Example usage:
delete_last_item(singly_linked_list)
singly_linked_list.iterate()

# 8. Create a doubly linked list, append items, and iterate through the list (print forward):


class DoublyNode:
    def __init__(self, data=None):
        self.data = data
        self.prev_node = None
        self.next_node = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = DoublyNode(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev_node = self.tail
            self.tail.next_node = new_node
            self.tail = new_node

    def iterate_forward(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" <-> ")
            current_node = current_node.next_node
        print("None")


# Example usage:
doubly_linked_list = DoublyLinkedList()
doubly_linked_list.append(1)
doubly_linked_list.append(2)
doubly_linked_list.append(3)

doubly_linked_list.iterate_forward()

# 9. Print nodes from the current position to the first node in a doubly linked list:


def iterate_backward(current_node):
    while current_node:
        print(current_node.data, end=" <-> ")
        current_node = current_node.prev_node
    print("None")


# Example usage:
current_node = doubly_linked_list.tail
iterate_backward(current_node)

# 10. Count the number of items in a given doubly linked list:


def count_items(doubly_linked_list):
    count = 0
    current_node = doubly_linked_list.head
    while current_node:
        count += 1
        current_node = current_node.next_node
    return count


# Example usage:
item_count = count_items(doubly_linked_list)
print("Number of items:", item_count)

# 11. Print a given doubly linked list in reverse order:


def print_reverse(doubly_linked_list):
    current_node = doubly_linked_list.tail
    while current_node:
        print(current_node.data, end=" <-> ")
        current_node = current_node.prev_node
    print("None")


# Example usage:
print_reverse(doubly_linked_list)

# 12. Insert an item in front of a given doubly linked list:


def insert_front(doubly_linked_list, data):
    new_node = DoublyNode(data)
    new_node.next_node = doubly_linked_list.head
    if doubly_linked_list.head:
        doubly_linked_list.head.prev_node = new_node
    doubly_linked_list.head = new_node


# Example usage:
insert_front(doubly_linked_list, 0)
doubly_linked_list.iterate_forward()

# 13. Search a specific item in a given doubly linked list:


def search_item_doubly(doubly_linked_list, target):
    current_node = doubly_linked_list.head
    while current_node:
        if current_node.data == target:
            return True
        current_node = current_node.next_node
    return False


# Example usage:
result = search_item_doubly(doubly_linked_list, 2)
print("Item found:", result)

# 14. Delete a specific item from a given doubly linked list:


def delete_item_doubly(doubly_linked_list, target):
    current_node = doubly_linked_list.head
    while current_node:
        if current_node.data == target:
            if current_node.prev_node:
                current_node.prev_node.next_node = current_node.next_node
            else:
                doubly_linked_list.head = current_node.next_node

            if current_node.next_node:
                current_node.next_node.prev_node = current_node.prev_node
            return True
        current_node = current_node.next_node
    return False


# Example usage:
result = delete_item_doubly(doubly_linked_list, 2)
if result:
    doubly_linked_list.iterate_forward()
else:
    print("Item not found.")
