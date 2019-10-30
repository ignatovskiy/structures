class Node:
    def __init__(self, element):
        self.item = element
        self.next_link = None


class StackLL:
    def __init__(self):
        self.head = None

    def is_empty(self):
        if self.head is None:
            print("Error! The list is empty!")
            return True
        else:
            return False

    def get_head(self):
        if StackLL.is_empty(self):
            return False
        else:
            print(self.head.item)
            return self.head.item

    def print_stack(self):
        if StackLL.is_empty(self):
            return False
        else:
            node = self.head
            while node is not None:
                print(node.item)
                node = node.next_link

    def search_item(self, element):
        if not StackLL.is_empty(self):
            node = self.head
            while node is not None:
                if node.item == element:
                    print("Found")
                    return True
                node = node.next_link
            print("Not found")
            return False

    def push(self, element):
        if self.head is None:
            self.head = Node(element)
        else:
            new_node = Node(element)
            new_node.next_link = self.head
            self.head = new_node

    def pop(self):
        if StackLL.is_empty(self):
            return False
        pop_head = self.head
        self.head = self.head.next_link
        pop_head.next_link = None
        print(pop_head.item)
        return pop_head
