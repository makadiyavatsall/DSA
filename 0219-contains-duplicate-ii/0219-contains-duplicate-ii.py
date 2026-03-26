class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Dictionary to store {number: last_seen_index}
        last_seen = {}
        
        for i, num in enumerate(nums):
            # If we've seen this number before and it's within distance k
            if num in last_seen and i - last_seen[num] <= k:
                return True
            
            # Update the dictionary with the current index
            last_seen[num] = i
            
        return False

