from bisect import bisect_left
from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        speeds = range(1, max(piles)+1)
        
        def can_finish(speed):

            hours_needed = 0
            for pile in piles:
                hours_needed += ceil(pile / speed)
            return hours_needed <= h

    
        index = bisect_left(speeds, True, key=can_finish)
        return speeds[index]
            

        