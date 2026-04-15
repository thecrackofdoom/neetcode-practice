from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity: int):
        self.lrucache = OrderedDict()
        self.slots = capacity

    def get(self, key: int) -> int:
        if key in self.lrucache:
            self.lrucache.move_to_end(key)
            return self.lrucache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.lrucache:
            self.lrucache[key] = value
        elif self.slots == 0:
            self.lrucache.popitem(last=False)
            self.lrucache[key] = value
        else:
            self.lrucache[key] = value
            self.slots -= 1
            

