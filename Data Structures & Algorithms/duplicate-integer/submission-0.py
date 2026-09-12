class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        from collections import Counter

        res = Counter(nums)

        for key, value in res.items():

            if value >= 2:
                return True

        return False
        