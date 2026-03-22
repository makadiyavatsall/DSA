class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mp = {0: -1}   # mod → index
        current_sum = 0

        for i, num in enumerate(nums):
            current_sum += num
            mod = current_sum % k

            if mod in mp:
                if i - mp[mod] >= 2:
                    return True
            else:
                mp[mod] = i

        return False
    



