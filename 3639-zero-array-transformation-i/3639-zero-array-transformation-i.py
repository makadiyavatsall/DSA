class Solution:
    def isZeroArray(self, nums, queries):
        n = len(nums)
        diff = [0] * (n + 1)   # difference array
        total = 0

        # Process all queries
        for l, r in queries:
            diff[l] += 1
            if r + 1 < len(diff):
                diff[r + 1] -= 1

        # Apply difference array and check feasibility
        for i in range(n):
            total += diff[i]
            if total < nums[i]:
                return False

        return True


