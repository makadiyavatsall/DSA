class Solution(object):
    def maxProduct(self, nums):
        if not nums:
            return 0

        # Initialize max, min, and result with the first element
        max_prod = min_prod = result = nums[0]

        # Traverse from the second element
        for i in range(1, len(nums)):
            num = nums[i]

            # When num is negative, swap max_prod and min_prod
            if num < 0:
                max_prod, min_prod = min_prod, max_prod

            # Update max_prod and min_prod for current position
            max_prod = max(num, max_prod * num)
            min_prod = min(num, min_prod * num)

            # Update result
            result = max(result, max_prod)

        return result



        