class Solution(object):
    def subsets(self, nums):
        res = []

        def backtrack(start, path):
            # Add the current subset
            res.append(list(path))

            # Explore further elements
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return res

        