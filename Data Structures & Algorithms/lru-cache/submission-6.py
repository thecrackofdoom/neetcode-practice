class Node:
    def __init__(self, key,val: int):
        self.val, self.key = val, key
        self.prev = self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.lrucache = {}
        self.cap = capacity
        self.tail = self.head = None
    def get(self, key: int) -> int:
        if key in self.lrucache:

            return self.lrucache[key].val
        else:
            return -1
    def put(self, key: int, value: int) -> None:
        if key in self.lrucache:
            self.lrucache[key].val = value
            temp_prev = self.lrucache[key].prev
            temp_next = self.lrucache[key].next
            self.lrucache[key].next = self.lrucache[key].prev = None

            self.tail.next = self.lrucache[key]
            self.tail = self.tail.next
            temp_prev.next = temp_next
            temp_next.prev = temp_prev
        elif self.cap == 0:
            del self.lrucache[self.head.key]
            self.head = self.head.next
            del self.head.prev
            

            self.lrucache[key] = Node(key = key, val = value)
            temp = self.tail
            self.tail = self.lrucache[key]
            temp.next = self.tail
            self.tail.prev = temp
        else:
            self.cap -= 1
            self.lrucache[key] = Node(key = key, val = value)

            if not self.head:
                self.head = self.lrucache[key]
                self.tail = self.lrucache[key]
            temp = self.tail
            self.tail = self.lrucache[key]
            temp.next = self.tail
            self.tail.prev = temp
        for k in self.lrucache.keys():
            print(k, self.lrucache[k].val)
        print()