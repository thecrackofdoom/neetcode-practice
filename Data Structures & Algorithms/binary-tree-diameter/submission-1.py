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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else:
            

            return max(self.maxdepth(root.right) + self.maxdepth(root.left), self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right))