class Solution(object):
    def findMiddleIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)   # total sum of array
        leftsum = 0         # sum of elements to the left

        for i in range(len(nums)):
            # sum of elements to the right
            rightsum = total - leftsum - nums[i]

            if leftsum == rightsum:
                return i

            # update leftsum for next iteration
            leftsum += nums[i]

        return -1
