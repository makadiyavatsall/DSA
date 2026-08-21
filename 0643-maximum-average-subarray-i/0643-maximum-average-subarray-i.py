class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        win = sum(nums[:k]) 
        Max = win
        for i in range(k,len(nums)):
            win = win + nums[i] - nums[i-k]
            Max = max(Max, win)
        return Max / k