class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        if n == 0:
            return
        
        k = k % n
        solution = []
        end = n - k

        for i in range(end, n):
            solution.append(nums[i])
        for j in range(0, end):
            solution.append(nums[j])

        # Write back into nums (in-place modification)
        nums[:] = solution

        