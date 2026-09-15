class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        res = set(nums)
        max_length = 0

        for num in res:

            # Only start if num is the START of a sequence
            if num - 1 not in res:

                current = num
                length = 1
                
                while current + 1 in res:
                    
                    length += 1
                    current += 1 
                    
                    
                max_length = max(max_length, length)   

        return max_length



        



        