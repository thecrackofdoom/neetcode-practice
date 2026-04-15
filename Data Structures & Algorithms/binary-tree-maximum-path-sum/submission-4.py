# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root:
            def branch(root):
                if root:
                    max_val = -10000
                    max_val = max(max_val, root.val)
                    if root.left:
                        max_val = max(max_val, root.val + branch(root.left))
                    if root.right:
                        max_val = max(max_val, root.val + branch(root.right))
                    return max_val
                else:
                    return 0
            return max(branch(root.left) + root.val + branch(root.right),
            self.maxPathSum(root.left),
            self.maxPathSum(root.right)
                )
        else:
            return -10000