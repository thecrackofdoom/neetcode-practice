# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root:
            return max(
            self.maxPathSum(root.right) + root.val,
            self.maxPathSum(root.left) + root.val,
            self.maxPathSum(root.left) + root.val + self.maxPathSum(root.right),
            self.maxPathSum(root.right),
            self.maxPathSum(root.left),
            root.val)
        else:
            return 0