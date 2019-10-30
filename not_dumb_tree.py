class NotDumbTree:
    def __init__(self, length):
        self.tree = [0] * length

    def create(self, element):
        self.tree[element] = element

    def union(self, old, new):
        self.tree[old] = new

    def search(self, index):
        while self.tree[index] != index:
            index = self.tree[index]
        return index


