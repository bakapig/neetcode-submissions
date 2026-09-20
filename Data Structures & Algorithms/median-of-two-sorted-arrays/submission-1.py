class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        merged = []
        left = 0
        right = 0
 
        while left<len(nums1) and right<len(nums2):

            if nums1[left]<nums2[right]:
                merged.append(nums1[left])
                left += 1
            else:
                merged.append(nums2[right])
                right += 1

        while left < len(nums1):
            merged.append(nums1[left])
            left += 1

        while right < len(nums2):
            merged.append(nums2[right])
            right += 1
            


        n = len(merged)
        if n%2 == 1:
            return merged[n//2]
        else:
            return (merged[n//2-1]+merged[n//2])*0.5

        # nums = nums1 + nums2
        # nums = sorted(nums)
        # print(nums)

        # n = len(nums)
        # mid = n//2

        # if n % 2 == 1:
        #     return nums[mid]

        # else:
        #     return (nums[mid-1]+nums[mid])/2

        