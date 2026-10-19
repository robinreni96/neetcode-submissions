class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        L = 0
        sum_tar = 0
        min_length = float("inf")

        for R in range(len(nums)):
            sum_tar += nums[R]
            while sum_tar >= target:
                min_length = min(R - L+1, min_length)
                sum_tar -= nums[L]
                L += 1
        
        return 0 if min_length == float("inf") else min_length

        