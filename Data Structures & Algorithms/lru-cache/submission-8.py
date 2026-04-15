class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.head = self.tail = None

    def insert(self, node):
        temp = self.tail
        self.tail = node
        temp.next = self.tail
        self.tail.prev = temp

    def remove(self, node):
        del self.cache[node.key]
        self.head = self.head.next
        del self.head.prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.insert(self.cache[key])
            self.cache[key].val = value
        elif self.cap == 0:
            self.remove(self.head)
            self.cache[key] = Node(key, value)
            self.insert(self.cache[key])
        else:
            self.cap -= 1
            self.cache[key] = Node(key, value)
            if not self.head:
                self.head = self.tail = self.cache[key]
            self.insert(self.cache[key])
