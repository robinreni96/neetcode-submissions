class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res_count = 0

        for i in range(0,len(arr)-k+1):
    
            avg_s_arr = sum(arr[i:i+k]) / k
            
            if avg_s_arr >= threshold:
                res_count += 1
        
        return res_count