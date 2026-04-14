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

        while p1 or p2:
            temp_sum = carry
            temp_sum += p1.val if p1 else 0
            temp_sum += p2.val if p2 else 0
            print(temp_sum)

            carry = temp_sum // 10
            temp_sum = temp_sum % 10

            sum.val = temp_sum
            if not head_sum:
                head_sum = sum

            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None

            if p1 or p2 or carry:
                sum.next = ListNode(0)
            sum = sum.next
        if carry:
            sum.val = carry
        return head_sum