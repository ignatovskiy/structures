class Node:
    def __init__(self, element):
        self.item = element
        self.next_link = None


class SingleLinkedList:
    def __init__(self):
        self.first_node = None

    def is_empty(self):
        if self.first_node is None:
            print("Error! The list is empty!")
            return True
        else:
            return False

    def search_item(self, element):
        if not SingleLinkedList.is_empty(self):
            node = self.first_node
            while node is not None:
                if node.item == element:
                    return True
                node = node.next_link
            return False

    def add_to_start(self, element):
        new_node = Node(element)
        new_node.next_link = self.first_node
        self.first_node = new_node

    def add_to_end(self, element):
        new_node = Node(element)
        if self.first_node is None:
            self.first_node = new_node
            return
        node = self.first_node
        while node.next_link is not None:
            node = node.next_link
        node.next_link = new_node

    def del_at_start(self):
        if not SingleLinkedList.is_empty(self):
            self.first_node = self.first_node.next_link

    def del_at_end(self):
        if not SingleLinkedList.is_empty(self):
            node = self.first_node
            while node.next_link.next_link is not None:
                node = node.next_link
            node.next_link = None

    def print_list(self):
        if not SingleLinkedList.is_empty(self):
            node = self.first_node
            while node is not None:
                print(node.item)
                node = node.next_link

