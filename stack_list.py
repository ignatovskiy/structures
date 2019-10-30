class StackList:
    def __init__(self):
        self.stack = list()

    def is_empty(self):
        if len(self.stack) == 0:
            print("Error! The Stack is empty!")
            return True
        else:
            return False

    def get_head(self):
        if StackList.is_empty(self):
            return False
        else:
            print(self.stack[-1])

    def print_stack(self):
        if StackList.is_empty(self):
            return False
        else:
            for element in reversed(self.stack):
                print(element)

    def search_item(self, element):
        if not StackList.is_empty(self):
            if element in self.stack:
                print("Found")
                return True
            else:
                print("Not found")
                return False

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if StackList.is_empty(self):
            return False
        pop_head = self.stack.pop()
        print(pop_head)
        return pop_head
