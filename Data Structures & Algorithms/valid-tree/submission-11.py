class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graphmap = {i: [] for i in range(n)}
        if len(edges) != n - 1:
            return False
        for e1, e2 in edges:
            graphmap[e1].append(e2)
            graphmap[e2].append(e1)

        visited = set()

        def dfs(cur, pa):
            if cur in visited:
                return False
            print(visited, cur, pa)
            for node in graphmap[cur]:
                if node != pa and dfs(node, cur):
                    visited.add(node)
            return True
        
        if dfs(0,-1) and len(visited) == n - 1:
            return True
        else:
            return False