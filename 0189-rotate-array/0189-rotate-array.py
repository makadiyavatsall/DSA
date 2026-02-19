class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        if n == 0:
            return
        
        k = k % n
        if k == 0:
            return
        
        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        
        # Step 1: Reverse whole array
        reverse(0, n - 1)
        
        # Step 2: Reverse first k elements
        reverse(0, k - 1)
        
        # Step 3: Reverse remaining n-k elements
        reverse(k, n - 1)

        