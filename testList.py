
#Insert head
#    Insert tail
#    Remove an element (By index or value, your choice)
#    Remove all duplicate nodes of the given value, retaining only the first occurrence
#    Search for an element, returning it's index if found
#    Size of the list


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    # insert element at the head
    def insert_head(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    # insert element at the tail
    def insert_tail(self, data):
        new_node = Node(data)
        if not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
    # remove element by value
    def remove_element(self, value):
        current = self.head
        while current:
            if current.data == value:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:  
                    self.head = current.next
                if current == self.tail:  
                    self.tail = current.prev
                return True  
            current = current.next
        return False  
    # remove all duplicate nodes of the given value, retaining only the first occurrence
    def remove_duplicate(self, value):
        seen = set()
        current = self.head
        while current:
            if current.data == value:
                if value in seen:
                    # Remove this node
                    next_node = current.next
                    self.remove_element(current.data)
                    current = next_node  
                else:
                    seen.add(value)
                    current = current.next  
            else:
                seen.add(current.data)
                current = current.next
    # search for an element, returning its index if found
    def search_element(self, value):
        index = 0
        current = self.head
        while current:
            if current.data == value:
                return index  
            index += 1
            current = current.next
        return -1  
    # size of the list
    def size_of_list(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count 
    # print the list
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()  # New line after printing the list

while True:
    selection = input("Insert 'ih' by add in head, \n, \
                   'it' by add in tail \n, \
                   'r' remove element\n, \
                   's' search element\n, \
                   'd' delete element\n, \
                   'c' count element in list, o\n \
                   'q' exit: ").lower()
    if selection == 'q':
        print("exiting..")
        break

    elif selection == 'ih':
    
        try:
            num = int(input("isert element: "))
            lista = DoublyLinkedList()
            lista.insert_head(num)
            print(f"number {num} saved in list.")
        except ValueError:
            print("Please, insert number valid.")
        except KeyboardInterrupt:
            print("\n exiting..")
            break
    elif selection == 'it':
        try:
            num = int(input("insert number by to save in list: "))
            lista.insert_tail(num)
            print(f"number {num} saved in list.")
        except ValueError:
            print("number not valid, try again.")
        except KeyboardInterrupt:
            print("\nexiting..")
            break
    elif selection == 'r':
        try:
            num = int(input("insert number to remove: "))
            if lista.remove_element(num):
                print(f"number removed: {num}")
            else:
                print(f"number {num} not found in list.")
        except ValueError:
            print("please, insert a valid number.")

    elif selection == 's':
        try:
            num = int(input("insert number to search: "))
            index = lista.search_element(num)
            if index != -1:
                print(f"Number {num} found at index {index}.")
            else:
                print(f"number {num} not found in list.")
        except ValueError:
            print("please, insert a valid number.")

    elif selection == 'd':
        try:
            num = int(input("insert number to delete duplicates: "))
            lista.remove_duplicate(num)
            print(f"duplicates of number {num} removed, retaining only the first occurrence.")
        except ValueError:
            print("please, insert a valid number.")

    elif selection == 'c':
        print(f"the size of list is: {lista.size_of_list()}")

    else:
        print("Selection not valid, try again.")
        continue

    lista.print_list()

#
