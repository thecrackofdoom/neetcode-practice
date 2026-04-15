import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i, stone in enumerate(stones):
            stones[i] = -stone
        
        heapq.heapify(stones)

        while len(stones) > 1:
            s1 = heapq.heappop(stones)
            s2 = heapq.heappop(stones)

            if s1 > s2:
                heapq.heappush(stones, s1 - s2)
            elif s2 > s1:
                heapq.heappush(stones, s2 - s1)
            print(stones)
        
        return abs(stones[0]) if stones else 0
