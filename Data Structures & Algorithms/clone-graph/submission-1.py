"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        map = {}
        cur = node

        def dfs(cur):
            if cur in map:
                return map[cur]
            
            map[cur] = Node(cur.val)
            for neighbor in cur.neighbors:
                temp = dfs(neighbor)
                
                map[cur].neighbors.append(temp)
            return map[cur]

        return dfs(cur)