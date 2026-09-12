class Solution:
    def maxArea(self, heights: List[int]) -> int:

        i = 0
        j = len(heights)-1
        max_area = 0

        while i < j:

            area = min(heights[i],heights[j]) * (j-i)
  
            max_area = max(max_area, area)

            if heights[i]<heights[j]:
                i += 1
            else:
                j -= 1

        return max_area


            






        
        # max_area = 0
        
        # for i, height in enumerate(heights):

        #     for j in range(i+1, len(heights)):

        #         vol = min(height, heights[j]) * (j-i)
        #         max_area = max(vol, max_area)


        # return max_area
