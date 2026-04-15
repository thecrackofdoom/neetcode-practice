class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.head = self.tail = Node(0, 0)
        self.head.next, self.tail.prev = self.tail, self.head

    def insert(self, node):
        temp_prev = self.tail.prev
        if node.prev and node.next:
            node_prev, node_next = node.prev, node.next
            node_prev.next, node_next.prev = node_next, node_prev

        temp_prev.next, self.tail.prev = node, node
        node.prev, node.next = temp_prev, self.tail



    def remove(self):
        self.head = self.head.next
        del self.cache[self.head.key]
        

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
            self.remove()
            self.cache[key] = Node(key, value)
            self.insert(self.cache[key])
        else:
            self.cap -= 1
            self.cache[key] = Node(key, value)
            self.insert(self.cache[key])
        print(self.cache)
