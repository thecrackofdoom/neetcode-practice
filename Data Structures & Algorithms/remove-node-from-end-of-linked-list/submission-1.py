# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        count = head
        while count:
            length += 1
            count = count.next
        
        remove_pos = length - n
        prev, curr = None, head
        for _ in range(remove_pos):
            prev = curr
            curr = curr.next
        if length == n:
            return head.next
        elif curr.next:
            prev.next = curr.next
        else:
            return None
        return head