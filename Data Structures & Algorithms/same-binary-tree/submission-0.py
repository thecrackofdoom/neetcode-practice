# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None or q is None:
            if p is not None:
                return False
            elif q is not None:
                return False
            else:
                return True

        pQueue = deque([p])
        qQueue = deque([q])

        while pQueue and qQueue:
            pNode = pQueue.popleft()
            qNode = qQueue.popleft()

            if pNode.val != qNode.val:
                return False

            if pNode.left and qNode.left and pNode.left.val == qNode.left.val:
                pQueue.append(pNode.left)
                qQueue.append(qNode.left)
            elif pNode.left != qNode.left:
                return False
            if pNode.right and qNode.right and pNode.right.val == qNode.right.val:
                pQueue.append(pNode.right)
                qQueue.append(qNode.right)
            elif pNode.right != qNode.right:
                return False

        return True