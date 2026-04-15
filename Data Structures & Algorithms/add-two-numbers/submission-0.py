# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0

        p1 = l1
        p2 = l2
        
        sum = ListNode(0)
        head_sum = None

        while p1 and p2:
            temp_sum = p1.val + p2.val + carry
            print(temp_sum)
            if temp_sum > 9:
                carry = temp_sum // 10
                temp_sum = temp_sum % 10
            sum.val = temp_sum
            if p1.next or carry:
                sum.next = ListNode(0)
            else:
                sum.next = None
            if not head_sum:
                head_sum = sum
            sum = sum.next
            p1 = p1.next
            p2 = p2.next
        if carry:
            sum.val = carry
        return head_sum