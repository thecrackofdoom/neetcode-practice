class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graphmap = {i: [] for i in range(n)}
        if n /2 == len(edges):
            return False
        for e1, e2 in edges:
            graphmap[e1].append(e2)
            graphmap[e2].append(e1)

        visited = set()
        def dfs(cur, con):
            
            print(visited, cur, con)
            if cur != con and cur in visited:
                return False
            
            for node in graphmap[cur]:
                visited.add(node)
                dfs(node, cur)
                
            return True
        
        for e1, e2 in edges:
            
            if not dfs(e1, e2) and not dfs(e2, e1):
                return False
            
        return True

            
