import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        
        for i in nums:
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1
        
        data = [[-cnt, key] for key, cnt in counts.items()]
        
        heapq.heapify(data)
        
        solution = []
        for i in range(k):
            solution.append(heapq.heappop(data)[1])
        
        return solution