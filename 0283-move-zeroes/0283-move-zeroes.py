class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        read, write = 0, 0
        n = len(nums)

        while read < n:

            if nums[read] != 0:
                nums[read], nums[write] = nums[write], nums[read]
                write += 1

            read += 1