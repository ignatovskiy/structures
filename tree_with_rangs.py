class RangsTree:
    def __init__(self, length):
        self.tree = [[0] * 2 for _ in range(length)]

    def create(self, element):
        self.tree[element][0] = element

    def union(self, old, new):
        if self.tree[old][1] < self.tree[new][1]:
            self.tree[old][0] = new
        elif self.tree[old][1] > self.tree[new][1]:
            self.tree[new][0] = old
        else:
            self.tree[old][0] = new
            self.tree[new][1] += 1

    def search(self, index):
        while self.tree[index][0] != index:
            index = self.tree[index][0]
        return index


