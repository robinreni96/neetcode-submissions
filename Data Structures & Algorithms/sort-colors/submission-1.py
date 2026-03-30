class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c = [0, 0, 0]

        for i in nums:
            c[i] += 1
        
        index = 0
        for i in range(0, len(nums)):
            while c[index] == 0:
                index += 1
            nums[i] = index
            c[index] -= 1
        
        