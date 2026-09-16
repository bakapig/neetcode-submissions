class KthLargest:

    from heapq import heapify, heappush, heappop

    def __init__(self, k: int, nums: List[int]):
        
        self.k = k
        self.heapify(nums)
        self.heap = nums
        print(nums)

        # Keep only the largest K elements
        while len(nums) > self.k:
            self.heappop(self.heap)        

    
    def add(self, val: int) -> int:

        self.heappush(self.heap, val)

        # Remove the smallest if heap grows beyond k
        if len(self.heap) > self.k:
            self.heappop(self.heap)

        return self.heap[0]





        
