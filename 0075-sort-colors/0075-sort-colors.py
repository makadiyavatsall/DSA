class Solution(object):
    def sortColors(self, nums):
        n = len(nums)
        for _ in range(n):  # multiple passes
            for k in range(n - 1):
                j = k + 1
                if nums[k] > nums[j]:  # simple swap if out of order
                    nums[k], nums[j] = nums[j], nums[k]
