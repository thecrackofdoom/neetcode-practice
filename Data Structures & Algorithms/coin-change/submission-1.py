class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount + 1)
        if not amount:
            return amount

        def dfs(amt):
            if amt == 0:
                return 0
            if dp[amt] != -1:
                return dp[amt]
            else:
                res = 1e8
                for coin in coins:
                    if coin <= amt:
                        res = min(res, 1 + dfs(amt - coin))
                dp[amt] = res
                return dp[amt]
        dfs(amount)
        return dp[-1] if dp[-1] < 1e8 else -1