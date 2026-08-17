class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        ans = []

        for itv in intervals:
            if len(ans) == 0:
                continue
            start, end = ans[-1]
            itv_s, itv_e = itv
            
            if start <= itv_s <= end:
                ans[-1][1] = itv_e
            if start >= itv_e >= end:
                ans[-1][0] = itv_s
            if itv_s < start and itv_e > end:
                ans[-1] = [itv_s, itv_e]
            if itv_s > end or itv_e < start:
                ans.append([itv_s, itv_e])
        return ans
            