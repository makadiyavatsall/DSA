class Solution(object):
    def moveZeroes(self, nums):
        i = 0  # slow pointer
        for j in range(len(nums)):  # fast pointer
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1



        
        