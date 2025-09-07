class NumArray:
    def __init__(self, nums):
        self.n = len(nums)
        self.nums = nums[:]               # copy of original array
        self.BIT = [0] * (self.n + 1)    # 1-indexed BIT array

        # Initialize BIT
        for i in range(self.n):
            self._addToBIT(i + 1, nums[i])

    # Internal function to update BIT
    def _addToBIT(self, index, val):
        while index <= self.n:
            self.BIT[index] += val
            index += index & -index       # move to next responsible node

    # Update value at index to val
    def update(self, index, val):
        diff = val - self.nums[index]
        self.nums[index] = val
        self._addToBIT(index + 1, diff)

    # Internal function to get prefix sum from 1 to index
    def _getPrefixSum(self, index):
        result = 0
        while index > 0:
            result += self.BIT[index]
            index -= index & -index       # move to parent
        return result

    # Get sum of nums[left..right]
    def sumRange(self, left, right):
        return self._getPrefixSum(right + 1) - self._getPrefixSum(left)

