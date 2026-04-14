# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode, maxUpperVal = - 10000) -> int:
        if root is None:
            return 0
        elif root.val >= maxUpperVal:
            return 1 + self.goodNodes(root.left , max(root.val, maxUpperVal)) + self.goodNodes(root.right , max(root.val, maxUpperVal))
        else:
            return self.goodNodes(root.left , max(root.val, maxUpperVal)) + self.goodNodes(root.right , max(root.val, maxUpperVal))