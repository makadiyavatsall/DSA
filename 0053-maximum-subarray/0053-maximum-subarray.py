class Solution(object):
    def maxSubArray(self, nums):
       current = nums[0]
       globall = nums[0]

       if not nums:
        return 0
       for i in range (1,len(nums)):
        num=nums[i]
        current = max(num,current + num)
        globall = max(current,globall)
       return globall
        
    




        