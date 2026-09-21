class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        result = []
        subset = []

        def backtrack(index):
            # We have made a decision for every number
            if index == len(nums):
                result.append(subset.copy())
                return

            # Choice 1: Include nums[index]
            subset.append(nums[index])
            backtrack(index+1)

            # Undo the previous choice
            subset.pop()

            # Choice 2: exclude nums[index]
            backtrack(index+1)


        backtrack(0)
        return result 











        # def backtrack(index):

        #     if finished:
        #         result.append(current.copy())
        #         return

        #     # Include
        #     current.append(nums[index])
        #     backtrack(index+1)

        #     # Backtrack
        #     current.pop()

        #     # Exclude
        #     backtrack(index+1)
        