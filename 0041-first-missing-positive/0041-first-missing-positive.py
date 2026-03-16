class Solution:
    def firstMissingPositive(self, nums):
        nums_set = set(nums)
        n = len(nums)

        for i in range(1, n + 2):
            if i not in nums_set:
                return i