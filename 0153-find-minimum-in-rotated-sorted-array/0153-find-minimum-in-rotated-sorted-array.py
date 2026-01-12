class Solution:
    def findMin(self, nums: List[int]) -> int:
        sorted_arr = sorted(nums)
        return sorted_arr[0]
