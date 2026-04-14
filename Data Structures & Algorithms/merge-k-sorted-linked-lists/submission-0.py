# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergetwo(self, list1: Optional[ListNode], list2: Optional[ListNode]):
        if not list1:
            return list2
        elif not list2:
            return list1
        
        headnew = new = ListNode(0)

        p1, p2 = list1, list2

        while p1 and p2:
            if p1.val >= p2.val:
                new.next = p2
                new = new.next
                p2 = p2.next
            else:
                new.next = p1
                new = new.next
                p1 = p1.next

        if not p1:
            new.next = p2
        elif not p2:
            new.next = p1
        return headnew.next
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        while len(lists) > 1:
            lists[0] = self.mergetwo(lists[0], lists[1])
            del lists[1]

        return lists[0] if lists else None