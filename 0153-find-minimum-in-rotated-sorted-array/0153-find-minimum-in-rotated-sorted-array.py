class Solution(object):
    def findMin(self, nums):
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                # Minimum is in right half
                left = mid + 1
            else:
                # Minimum is in left half (including mid)
                right = mid

        return nums[left]

        