
class Device:
    def __init__(self, source, target, weight, int):
        self.source = source
        self.target = target
        self.weight = weight
        self.int = int

        self.neighbor = []

    def add_neighbor(self, new_neigh):
        self.new_neigh = new_neigh
        self.neighbor.append(new_neigh)
