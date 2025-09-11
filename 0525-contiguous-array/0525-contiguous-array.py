class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix_sum = 0
        first_occurrence = {0: -1}   
        max_len = 0

        for i in range(len(nums)):
            num = nums[i]

            
            if num == 1:
                prefix_sum += 1
            else:
                prefix_sum -= 1

            if prefix_sum in first_occurrence:
                max_len = max(max_len, i - first_occurrence[prefix_sum])
            else:
                first_occurrence[prefix_sum] = i

        return max_len

       