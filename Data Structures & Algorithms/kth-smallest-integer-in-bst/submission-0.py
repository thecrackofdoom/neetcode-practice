# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    arr = []
    def inorder(self, root):
        if root is None:
            return
        else:
            self.inorder(root.left)
            solution.arr.append(root.val)
            self.inorder(root.right)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.inorder(root)
        print(solution.arr)
        return solution.arr[k-1]