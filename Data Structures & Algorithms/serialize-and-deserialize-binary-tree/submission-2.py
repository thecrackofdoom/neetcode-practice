# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''
        queue = deque([root])
        tree_str = []
        temp_str = [root.val]
        r = 1 #node remains in layer
        temp_r = 0 # storing number of nodes in next layer
        while queue:
            
            node = queue.popleft()
            r -= 1

            if node.left:
                queue.append(node.left)
                temp_r += 1
                temp_str.append(node.left.val)
            else:
                temp_str.append("*")
                

            if node.right:
                queue.append(node.right)
                temp_r += 1
                temp_str.append(node.right.val)
            else:
                temp_str.append("*")
            
            print(f"Number of nodes left in layer: {r} and temp number next layer {temp_r}")
            if r == 0:
                r = temp_r
                temp_r = 0
                tree_str.extend(temp_str)
                temp_str = []
        
        return ''.join(str(val) for val in tree_str).strip('*')
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return 
        data = list(data)
        root = TreeNode(int(data[0]))
        queue = deque([root])
        ptr = 1
        while queue and ptr < len(data):
            node = queue.popleft()

            if data[ptr] != '*':
                node.left = TreeNode(int(data[ptr]))
                ptr += 1
                queue.append(node.left)
            else:
                ptr += 1
            if data[ptr] != '*':
                node.right = TreeNode(int(data[ptr]))
                ptr += 1
                queue.append(node.right)
            else:
                ptr += 1
        return root
            