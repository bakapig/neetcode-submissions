class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        from collections import defaultdict
        from math import sqrt, pow
        from heapq import heapify, heappop, heappush
        distance = defaultdict(tuple)

        for i, point in enumerate(points):

            distance[i] = (sqrt((pow(point[0], 2) + pow(point[1], 2))), i)

            
        print(distance)
        res = [value for key, value in distance.items()]
        heapify(res)
        final = []
        

        for i in range(k):
            x = heappop(res)
            print(x)
            
        
            for key, value in distance.items():
                if value == x:
                    target_key = key
                    final.append(points[key])
            
        return final