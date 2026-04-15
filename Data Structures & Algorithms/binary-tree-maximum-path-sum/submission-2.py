# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    sum = - 100000
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        solution.sum = -100000
        if root:
            solution.sum = max(solution.sum, root.val)
        
            if root.right:
                right = self.maxPathSum(root.right)
                solution.sum = max(solution.sum, root.val + right)

            if root.left:
                left = self.maxPathSum(root.left)
                solution.sum = max(solution.sum, root.val + left)

            if root.left and root.right:
                solution.sum = max(solution.sum, left + root.val + right)

            return solution.sum


        else:
            return 