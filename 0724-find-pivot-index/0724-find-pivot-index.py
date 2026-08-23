class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        n = len(nums)

        prefix = [0] * n
        Total = sum(nums)

        for i in range(1, n):
            prefix[i] = prefix[i-1] + nums[i-1]

        for i in range(n):
            right = Total - prefix[i] - nums[i]

            if prefix[i] == right:
                return i

        return -1