import random
import math


class Node:
    def __init__(self, item, height):
        self.item = item
        self.next = [None] * (height + 1)


class SkipList:
    def __init__(self, size):
        self.max_height = int(math.log(size, 2))
        self.possibility = 0.5
        self.header = Node(-1, self.max_height)
        self.height = 0

    def random(self):
        height = 0
        while random.random() < self.possibility and height < self.max_height:
            height += 1
        return height

    def insert(self, item):
        current = self.header
        update = [None] * (self.max_height + 1)
        for index in range(self.height, -1, -1):
            while current.next[index] and current.next[index].item < item:
                current = current.next[index]
            update[index] = current
        current = current.next[0]
        if current is None or current.item != item:
            height = self.random()
            if height > self.height:
                for index in range(self.height + 1, height + 1):
                    update[index] = self.header
                self.height = height
            node = Node(item, height)
            for index in range(height + 1):
                node.next[index], update[index].next[index] = update[index].next[index], node

    def delete(self, item):
        update = [None] * (self.max_height + 1)
        current = self.header
        for index in range(self.height, -1, -1):
            while current.next[index] and current.next[index].item < item:
                current = current.next[index]
            update[index] = current
        current = current.next[0]
        if current is not None and current.item == item:
            for index in range(self.height + 1):
                if update[index].next[index] != current:
                    break
                update[index].next[index] = current.next[index]
            while self.height > 0 and self.header.next[self.height] is None:
                self.height -= 1

    def search(self, item):
        current = self.header
        for index in range(self.height, -1, -1):
            while current.next[index] and current.next[index].item < item:
                current = current.next[index]
        current = current.next[0]
        if current and current.item is item:
            return True
        return False

    def print_list(self):
        head = self.header
        for height in range(self.height, -1, -1):
            print("Height {} - ".format(height + 1), end=' ')
            node = head.next[height]
            while node is not None:
                print(node.item, end=' ')
                node = node.next[height]
            print("\n")





