class Solution:
    def minZeroArray(self, nums, queries):
        n = len(nums)
        left, right = 0, len(queries)

        if not self.can_make_zero(nums, queries, right):
            return -1

        while left <= right:
            mid = (left + right) // 2
            if self.can_make_zero(nums, queries, mid):
                right = mid - 1
            else:
                left = mid + 1

        return left

    def can_make_zero(self, nums, queries, k):
        n = len(nums)
        diff = [0] * (n + 1)

        for i in range(k):
            start, end, val = queries[i]
            diff[start] += val
            if end + 1 < len(diff):
                diff[end + 1] -= val

        curr_sub = 0
        for i in range(n):
            curr_sub += diff[i]
            if curr_sub < nums[i]:
                return False
        return True
