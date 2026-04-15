# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root_val = preorder[0]
        out = []
        def finder(root_val, arr, k = 1):
            if len(arr) == 1:
                out.append(arr[0])
                
                return arr[0]
            node_val = preorder[k]
            if arr.index(root_val) > arr.index(node_val):
                finder(node_val, arr[ : arr.index(root_val)], k + 1)
            else:
                finder(node_val, arr[arr.index(root_val) + 1 : ], k + 1)
        finder(root_val, preorder, 1)
        print(out)