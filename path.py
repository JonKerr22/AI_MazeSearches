from utils import accepts_tuple_arg
from time import sleep
from sets import Set
class Path:
    @accepts_tuple_arg
    def __init__(self, prev, x, y):
        self.length = len(prev) + 1 if prev != None else 0
        self.dependents = Set([])
        self.prev = prev
        self.coord = (x,y)
        if prev != None:
            self.prev.dependents.add(self)
    def __len__(self):
        return self.length
    def __iter__(self):
        return _PathIterator(self)

    def __add__(self, other):
        prev = self
        for coord in other:
            curr = Path(prev, coord)
            prev = curr
        return prev
    
    def updatePath(self, other):
        if other != self.prev:
            if other.length >= self.prev.length:
                return
            self.prev = other
            other.dependents.add(self)
        self.length = len(other) + 1
        for dep in self.dependents:
            dep.updatePath(self)
class _PathIterator:
    def __init__(self, path):
        self._curNode = path
    def next(self):
        return self.__next__();
    def __next__(self):
        if self._curNode == None:
            raise StopIteration
        else: 
            item = self._curNode
            self._curNode = self._curNode.prev
            return item.coord

if __name__ == "__main__":
    a = Path(None, 1, 0)
    b = Path(a, 2, 0)
    c = Path(b, 3, 0)
    d = Path(c, 4, 0)
    e = Path(d, 5, 0)
    print(len(e))
    print(c.dependents)
    c.updatePath(a)
    print(len(e))
    f = e+[(6,0)]
    for x in f:
        print(x)

    
