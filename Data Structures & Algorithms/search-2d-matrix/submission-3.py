class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        from bisect import bisect_left

        res = []

        for lst in matrix:
            for item in lst:
                res.append(item)

        idx = bisect_left(res, target)
        # idx >= len(nums) or target != nums[idx]
        if idx >= len(res) or res[idx] != target:
            return False
        else:
            return True