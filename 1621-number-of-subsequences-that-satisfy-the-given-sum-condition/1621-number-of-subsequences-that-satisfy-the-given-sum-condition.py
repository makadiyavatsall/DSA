from typing import List

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10**9 + 7
        nums.sort()
        n = len(nums)
        
        # Precompute powers of 2 for efficiency
        power = [1] * n
        for i in range(1, n):
            power[i] = (power[i - 1] * 2) % MOD
        
        res = 0
        i, j = 0, n - 1
        
        while i <= j:
            if nums[i] + nums[j] <= target:
                # All subsequences between i and j are valid
                res = (res + power[j - i]) % MOD
                i += 1
            else:
                j -= 1
        
        return res
