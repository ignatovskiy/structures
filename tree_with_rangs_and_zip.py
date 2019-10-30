class RangsZipTree:
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
        temp1 = index
        temp2 = index
        while self.tree[index][0] != index:
            index = self.tree[index][0]
        while self.tree[temp1][0] != temp1:
            temp_new = temp1
            temp1 = self.tree[temp1][0]
            self.tree[temp_new][0] = temp2
        return index

