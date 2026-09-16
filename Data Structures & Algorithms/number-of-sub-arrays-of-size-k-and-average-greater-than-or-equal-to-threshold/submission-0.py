class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res_count = 0

        for i in range(0,len(arr)-k+1):

            s_arr = arr[i:i+k]
    
            avg_s_arr = sum(s_arr) / k
            
            if avg_s_arr >= threshold:
                res_count += 1
        
        return res_count