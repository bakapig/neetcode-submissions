class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        from collections import Counter
        res = Counter(nums)

        for key, val in res.items():
            if val > 1:
                return key
        