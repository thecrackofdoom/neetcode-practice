"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        pointer = head
        new = Node(0)
        head_new = None
        node_dict = {}

        while pointer:
            new.val = pointer.val
            new.next = Node(0) if pointer.next else None

            if not head_new:
                head_new = new

            node_dict[pointer] = new

            new = new.next
            pointer = pointer.next

        pointer = head
        new = head_new
        while pointer:
            if pointer.random in node_dict:
                new.random = node_dict[pointer.random]
            else:
                new.random = None
            
            pointer = pointer.next
            new = new.next
        return head_new
