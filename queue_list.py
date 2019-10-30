class QueueList:
    def __init__(self):
        self.queue = list()

    def is_empty(self):
        if len(self.queue) == 0:
            print("Error! The Queue is empty!")
            return True
        else:
            return False

    def print_queue(self):
        if QueueList.is_empty(self):
            return False
        else:
            for element in self.queue:
                print(element)

    def search_item(self, element):
        if not QueueList.is_empty(self):
            if element in self.queue:
                print("Found")
                return True
            else:
                print("Not found")
                return False

    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        if QueueList.is_empty(self):
            return False
        dequeue_head = self.queue.pop(0)
        print(dequeue_head)
        return dequeue_head

