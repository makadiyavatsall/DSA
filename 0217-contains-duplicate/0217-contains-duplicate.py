class Solution:
    def containsDuplicate(self, nums):
        seen = {}
        for x in nums:
            if x in seen:
                return True
            seen[x] = 1
        return False
