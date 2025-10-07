class Solution(object):
    def countQuadruplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        count = 0

        for i in range(n-3):
            for j in range(i+1, n-2):
                for k in range(j+1, n-1):
                    sum3 = nums[i] + nums[j] + nums[k]
                    # check if sum3 exists in remaining elements
                    for l in range(k+1, n):
                        if sum3 == nums[l]:
                            count += 1
        return count

        