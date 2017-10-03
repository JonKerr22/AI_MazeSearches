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
    def __str__(self):
        l = []
        for coord in self:
            l += coord
        l.reverse()
        return str(list(l)[2:])
    def updatePath(self, other):
        if self.prev != None and other.coord != self.prev.coord:
            if other.length >= self.prev.length:
                return
            self.prev = other.prev
            self.coord = other.coord
            other.dependents.add(self)
        self.length = len(other) + 1
        #for dep in self.dependents:
        #    return dep.updatePath(self)


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
    a = Path(None, 2, 1)
    b = Path(a, 1, 1)
    c = Path(b, 1, 2)
    d = Path(c, 1, 3)
    e = Path(d, 2, 3)
    f = Path(e, 3, 3)

    g = Path(a, 2, 2)
    print("E:" + str(e))
    print("F:" + str(f))
    print("G:" + str(g))
    e.updatePath(g)
    print(f)

    
