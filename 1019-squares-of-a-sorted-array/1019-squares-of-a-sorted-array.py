class Solution(object):
    def sortedSquares(self, nums):
       sqr = [num**2 for num in nums]
       sqr.sort()
       return sqr