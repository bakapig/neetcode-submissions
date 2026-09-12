class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        from heapq import heapify, heappop

        tmp = [-num for num in nums]
        heapify(tmp)

        for i in range(k):

            res = heappop(tmp)

        return -res