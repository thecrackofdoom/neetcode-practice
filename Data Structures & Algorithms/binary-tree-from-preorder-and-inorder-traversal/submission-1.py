# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        node_map = {value: index for index, value in enumerate(inorder)}
        self.pre_loc = 0

        def build(l, r):
            if l > r:
                return
            else:
                root_val = preorder[self.pre_loc]
                self.pre_loc += 1
                root_index = node_map[root_val]

                root = TreeNode(root_val)
                root.left = build(l, root_index - 1)
                root.right = build(root_index + 1, r)
                return root
        return build(0, len(inorder) - 1)


