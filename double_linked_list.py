class Node:
    def __init__(self, element):
        self.item = element
        self.next_link = None
        self.prev_link = None


class DoubleLinkedList:
    def __init__(self):
        self.first_node = None

    def is_empty(self):
        if self.first_node is None:
            print("Error! The list is empty!")
            return True
        else:
            return False

    def search_item(self, element):
        if not DoubleLinkedList.is_empty(self):
            node = self.first_node
            while node is not None:
                if node.item == element:
                    return True
                node = node.next_link
            return False

    def print_list(self):
        if not DoubleLinkedList.is_empty(self):
            node = self.first_node
            while node is not None:
                print(node.item)
                node = node.next_link

    def add_to_empty(self, element):
        new_node = Node(element)
        self.first_node = new_node

    def add_to_start(self, element):
        if self.first_node is None:
            DoubleLinkedList.add_to_empty(self, element)
            return
        new_node = Node(element)
        new_node.next_link = self.first_node
        self.first_node.prev_link = new_node
        self.first_node = new_node

    def add_to_end(self, element):
        if self.first_node is None:
            DoubleLinkedList.add_to_empty(self, element)
            return
        new_node = Node(element)
        node = self.first_node
        while node.next_link is not None:
            node = node.next_link
        node.next_link = new_node
        new_node.prev_link = node

    def del_at_start(self):
        if not DoubleLinkedList.is_empty(self):
            if self.first_node.next_link is None:
                self.first_node = None
                return
            self.first_node = self.first_node.next_link
            self.first_node.prev_link = None

    def del_at_end(self):
        if not DoubleLinkedList.is_empty(self):
            if self.first_node.next_link is None:
                self.first_node = None
                return
            node = self.first_node
            while node.next_link is not None:
                node = node.next_link
            node.prev_link.next_link = None
