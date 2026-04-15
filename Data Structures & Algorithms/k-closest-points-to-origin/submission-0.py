import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = [(point[0] * 2 + point[1] * 2, point) for point in points]
        heapq.heapify(dist)
        return [heapq.heappop(dist)[1] for _ in range(k)]