# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        queue = deque([root])
        
        res = []
        while queue:
            temp_arr = [] #storing the childs before actually appending
            layer = [] #curr layer
            while queue:
                node = queue.popleft()
                layer.append(node.val)

                if node.left:
                    temp_arr.append(node.left)
                if node.right:
                    temp_arr.append(node.right)
            res.append(layer)
            queue.extend(temp_arr)
        return res

            
