class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxPile = max(piles)
        minPile = min(piles)
        low, high = minPile, maxPile

        while low <= high:
            mid = (low + high) // 2
            hours_taken = sum(int(-(-pile // mid)) for i, pile in enumerate(piles))
            if hours_taken == h:
                return mid
            elif hours_taken > h:
                low = mid + 1
            else:
                return mid
