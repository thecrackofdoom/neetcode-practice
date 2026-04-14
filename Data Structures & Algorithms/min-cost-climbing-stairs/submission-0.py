class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        arr = [0] * len(cost)
        def dfs(i):
            if i >= len(cost):
                return 0
            if arr[i] != 0:
                return arr[i]
            
            
            arr[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))
            return arr[i]
        return min(dfs(0), dfs(1))