class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1  # Base case: 1 step, 1 way (1)
        
        # Initialize the number of ways for the first two steps
        # ways_n_minus_2 represents ways to reach step i-2
        # ways_n_minus_1 represents ways to reach step i-1
        ways_n_minus_2 = 1  # F(1) - Ways to reach step 1
        ways_n_minus_1 = 2  # F(2) - Ways to reach step 2
        
        # Start from step 3 up to step n
        for i in range(3, n + 1):
            # The number of ways to reach the current step 'i'
            current_ways = ways_n_minus_1 + ways_n_minus_2
            
            # Update for the next iteration
            ways_n_minus_2 = ways_n_minus_1
            ways_n_minus_1 = current_ways
            
        return ways_n_minus_1