class Solution:
    def rob(self, nums: List[int]) -> int:

        memo = {}

        def rob_from(i):

            if i >= len(nums):
                return 0

            if i in memo:
                return memo[i]

            # Choice 1 rob now
            rob_now = nums[i] + rob_from(i+2)

            # Choice 2 rob later
            rob_later = rob_from(i+1)

            memo[i] = max(rob_now, rob_later)

            # Choose optimal
            return memo[i]


        return rob_from(0)

        