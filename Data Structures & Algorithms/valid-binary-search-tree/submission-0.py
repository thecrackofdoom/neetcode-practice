# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def validation (self, root, parent, branch):
        if root is None:
            return True
        if root.left:
            if root.left.val >= root.val:
                return False
        if root.right:
            if root.right.val <= root.val:
                return False
        if branch == 'left' and root.right and root.right >= parent.val:
            return False
        if branch == 'right' and root.left and root.left <= parent.val:
            return False
        return self.validation(root.right, root, 'right') and self.validation(root.left, root, 'left')
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.validation(root, None, None)