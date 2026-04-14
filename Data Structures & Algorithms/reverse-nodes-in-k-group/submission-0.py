# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, tail_left, left, right):
        prev = None
        curr = left

        while curr and curr != right:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        left.next = right
        if tail_left:
            tail_left.next = prev
        return prev
        
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        tail_left = None
        left = head
        temp = left
        for _ in range(k):
            if temp:
                temp = temp.next
            else:
                return None
        right = temp
        while True:
            node = self.reverse(tail_left, left, right)
            if not tail_left:
                head = node
            tail_left = left
            left = right
            temp = left
            for _ in range(k):
                if temp:
                    temp = temp.next
                else:
                    return head
            right = temp

            p = head
            for _ in range(6):
                print(p.val if p else None)
                p = p.next if p else None
            


        