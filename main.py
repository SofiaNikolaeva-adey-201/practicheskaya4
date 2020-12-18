class Table:
    def __init__(self, l, w, h):
        self.length = l
        self.width = w
        self.height = h

class KitchenTable(Table):
    def __init__(self, l, w, h, p):
        self.length = l
        self.width = w
        self.height = h
        self.places = p
    def square(self):
        return self.length*self.width


class DeskTable(Table):
    def square(self):
        return self.width * self.length

class ComputerTable(Table):
    def square(self, e):
        return DeskTable.square(self) - e

ct = ComputerTable(2, 1, 1)
print(ct.square(0.3))

t1 = KitchenTable(2, 2, 0.7, 1)
print(t1.square())
t2 = DeskTable(1.5, 0.8, 0.75)
print(t2.square())
t3 = KitchenTable(1, 1.2, 0.8, 1)
print(t3.square())