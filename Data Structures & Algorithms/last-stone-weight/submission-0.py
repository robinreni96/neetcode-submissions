class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        arr = stones

        heapq.heapify_max(arr)

        while len(arr) > 1:

            y = heapq.heappop_max(arr)
            x = heapq.heappop_max(arr)

            if x < y:
                z = y - x
                heapq.heappush_max(arr, z)
        
        arr.append(0)
        return abs(arr[0])
        