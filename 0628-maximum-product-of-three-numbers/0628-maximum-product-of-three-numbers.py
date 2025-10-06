class Solution(object):
    def maximumProduct(self, nums):
        if not nums:
            return 0

        nums.sort()
        n = len(nums)

        # Two possible max products
        product1 = nums[n-1] * nums[n-2] * nums[n-3]  # three largest
        product2 = nums[0] * nums[1] * nums[n-1]      # two smallest + largest

        return  max(product1, product2)
