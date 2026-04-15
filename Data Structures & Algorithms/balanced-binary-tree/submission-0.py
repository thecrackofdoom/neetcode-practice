# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxdepth(self, root):
        if root is None:
            return 0
        else:
            return 1 + max(self.maxdepth(root.right), self.maxdepth(root.left))
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        else:
            return True if abs(self.maxdepth(root.left) - self.maxdepth(root.right)) <= 1 else False