class Solution:
    def search(self, nums: List[int], target: int) -> int:

        from bisect import bisect_left

        idx = bisect_left(nums, target)
        print(idx)

        if idx >= len(nums) or target != nums[idx]:
            return -1
        else:
            return idx


        