class Node:
    def __init__(self, element):
        self.item = element
        self.next_link = None


class CircularLinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next_link = self.tail
        self.tail.next_link = self.head

    def is_empty(self):
        if self.head.item is None:
            print("Error! The list is empty!")
            return True
        else:
            return False

    def search_item(self, element):
        if not CircularLinkedList.is_empty(self):
            node = self.head
            if node.item == element:
                print("Found")
                return True
            node = node.next_link
            while node is not self.head:
                if node.item == element:
                    print("Found")
                    return True
                node = node.next_link
            print("Not found")
            return False

    def print_list(self):
        if not CircularLinkedList.is_empty(self):
            print(self.head.item)
            node = self.head.next_link
            while node is not self.head:
                print(node.item)
                node = node.next_link

    def add_to_empty(self, element):
        new_node = Node(element)
        self.head = new_node
        self.tail = new_node
        new_node.next_link = self.head

    def add_to_start(self, element):
        if self.head.item is None:
            CircularLinkedList.add_to_empty(self, element)
        else:
            new_node = Node(element)
            self.tail.next_link = new_node
            new_node.next_link = self.head
            self.head = new_node

    def add_to_end(self, element):
        if self.tail.item is None:
            CircularLinkedList.add_to_empty(self, element)
        else:
            new_node = Node(element)
            self.tail.next_link = new_node
            self.tail = new_node
            new_node.next_link = self.head

    def del_at_start(self):
        if not CircularLinkedList.is_empty(self):
            if self.tail is self.head:
                self.head.item = None
                return
            self.tail.next_link = self.head.next_link
            self.head = self.head.next_link

    def del_at_end(self):
        if not CircularLinkedList.is_empty(self):
            if self.tail is self.head:
                self.head.item = None
                return
            node = self.tail
            while node.next_link is not self.tail:
                node = node.next_link
            node.next_link = self.head
            self.tail = node










