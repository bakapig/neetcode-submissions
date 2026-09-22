class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        from collections import Counter

        res = Counter(nums)

        ans = [key for key, value in res.items() if value == 1]

        return ans[0]
        