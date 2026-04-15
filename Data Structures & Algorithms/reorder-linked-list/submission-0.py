# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        
        second_half_head = slow if fast else slow.next
        prev, curr = None, second_half_head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        p1 = head
        p2 = prev
        
        while p2:
            temp1 = p1.next
            temp2 = p2.next

            p1.next = p2
            p2.next = temp1

            p1 = temp1
            p2 = temp2
            

        
            
