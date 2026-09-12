class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        from heapq import heapify, heappop, heappush
        stones = [-stone for stone in stones]
        heapify(stones)

        while len(stones) > 1:
            y = -heappop(stones)
            x = -heappop(stones)

            if y - x:
                heappush(stones, -(y-x))

            elif y == x:
                continue

        if len(stones) == 1:
            return -heappop(stones)
        elif len(stones) == 0:
            return 0