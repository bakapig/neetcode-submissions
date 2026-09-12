class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        from collections import Counter

        res = Counter(nums)
        final = res.most_common(k)
        return [item[0] for item in final]



        



        