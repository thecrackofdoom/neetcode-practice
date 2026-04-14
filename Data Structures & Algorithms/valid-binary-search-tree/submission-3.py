# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(curr, range):
            if not curr:
                return True
            if range[0] < curr.val < range[1]:
                return dfs(curr.left, (range[0], curr.val)) and dfs(curr.right, (curr.val, range[1]))
            else:
                return False
        return dfs(root, (-10000, 10000))