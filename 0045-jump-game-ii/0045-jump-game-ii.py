class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float('inf')] * n
        dp[-1] = 0  # base case: already at last index

        for i in range(n - 2, -1, -1):
            max_jump = nums[i]
            for j in range(i + 1, min(n, i + max_jump + 1)):
                dp[i] = min(dp[i], 1 + dp[j])

        return dp[0]