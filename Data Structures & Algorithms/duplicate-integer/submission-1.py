class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        from collections import Counter

        res = Counter(nums)

        for value in res.values():
            if value > 1:
                return True

        return False