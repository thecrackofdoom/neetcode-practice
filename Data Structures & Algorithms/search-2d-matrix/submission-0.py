class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t, b = 0, len(matrix) - 1
        arr = []
        while t <= b:
            mid = (t + b) // 2
            if matrix[mid][0] <= target <= matrix[mid][len(matrix[mid]) - 1]:
                arr = matrix[mid]
                break
            elif matrix[mid][0] > target:
                b = mid - 1
            elif matrix[mid][len(matrix[mid]) - 1] < target:
                t = mid + 1
        
        l, r = 0, len(arr) - 1
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                l = mid + 1
            elif arr[mid] > target:
                r = mid - 1
        return False