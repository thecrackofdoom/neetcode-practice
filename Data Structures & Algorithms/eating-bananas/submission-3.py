class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxPile = max(piles)
        minPile = 1
        low, high = minPile, maxPile
        min_rate = max(piles)

        while low <= high:
            mid = (low + high) // 2
            hours_taken = sum(int(-(-pile // mid)) for i, pile in enumerate(piles))
            if hours_taken == h:
                min_rate = min(min_rate, mid)
                high = mid - 1
            elif hours_taken > h:
                low = mid + 1
            else:
                min_rate = min(min_rate, mid)
                high = mid - 1
        return min_rate
            
