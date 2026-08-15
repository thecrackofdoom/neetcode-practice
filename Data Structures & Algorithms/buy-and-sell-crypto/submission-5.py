class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0
        left, right = 0, 1
        while left < len(prices):
            if prices[left] < prices[right]:
                max_p = max(max_p, prices[right] - prices[left])
            elif prices[left] > prices[right]:
                left = right
            
            right += 1
        return max_p
            