class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(numbers) - 1

        while left < right:
            current = numbers[left] + numbers[right]
            
            if current == target:
                # return 1-based indices as per problem
                return [left + 1, right + 1]
            elif current < target:
                left += 1
            else:
                right -= 1

        return [-1, -1]  # if no solution found
