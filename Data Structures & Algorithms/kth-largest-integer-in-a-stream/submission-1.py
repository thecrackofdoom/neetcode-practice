import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq._heapify_max(nums)
        self.nums = nums
        self.k = k
    def kth(self, heap):
        arr = []
        
        for _ in range(self.k):
            
            num = heapq.heappop_max(heap)
            arr.append(num)

        for i in range(self.k - 1, -1, -1):
            heapq.heappush_max(heap, arr[i])
            
        
        return num


    def add(self, val: int) -> int:
        heapq.heappush_max(self.nums, val)
        print(self.nums)

        return self.kth(self.nums)

