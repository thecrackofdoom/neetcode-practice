# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new = ListNode(0)
        l1 = list1
        l2 = list2
        headnew = new
        if not l1:
            return l2
        elif not l2:
            return l1
        while l1 and l2:
            if l1.val >= l2.val:
                if not new:
                    new = l2
                else:
                    new.next = l2
                    new = new.next
                l2 = l2.next
            else:
                if not new:
                    new = l1
                else:
                    new.next = l1
                    new = new.next
                l1 = l1.next
            if not l1:
                new.next = l2
            elif not l2:
                new.next = l1
        return headnew.next