class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        from heapq import heapify, heappop, heappush
        stones = [-stone for stone in stones]
        heapify(stones)

        while len(stones) > 1:
            y = -heappop(stones)
            x = -heappop(stones)
            if x == y:
                continue
            elif x < y:
                heappush(stones, -(y-x))

        if len(stones) == 1:
            return -stones[0]
        else:
            return 0
            
        
        