class Node:
    def __init__(self, element):
        self.item = element
        self.next_link = None


class QueueLL:
    def __init__(self):
        self.head = None

    def is_empty(self):
        if self.head is None:
            print("Error! The queue is empty!")
            return True
        else:
            return False

    def print_queue(self):
        if not QueueLL.is_empty(self):
            node = self.head
            while node is not None:
                print(node.item)
                node = node.next_link

    def search_item(self, element):
        if not QueueLL.is_empty(self):
            node = self.head
            while node is not None:
                if node.item == element:
                    print("Found")
                    return True
                node = node.next_link
            print("Not found")
            return False

    def enqueue(self, element):
        new_node = Node(element)
        node = self.head
        if node is None:
            self.head = new_node
        else:
            while node.next_link is not None:
                node = node.next_link
            node.next_link = new_node

    def dequeue(self):
        node = self.head
        if not QueueLL.is_empty(self):
            self.head = node.next_link
        print(node.item)
        return node.item
