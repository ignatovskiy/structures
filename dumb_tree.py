class DumbTree:
    def __init__(self, length):
        self.massive = [0] * length

    def create(self, element):
        self.massive[element] = element

    def union(self, old, new):
        for index in range(len(self.massive)):
            if self.massive[index] == old:
                self.massive[index] = new

    def search(self, index):
        return self.massive[index]

