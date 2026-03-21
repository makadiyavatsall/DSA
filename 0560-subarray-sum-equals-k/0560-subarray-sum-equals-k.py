class Solution:   
    def subarraySum(self, nums, k) -> int:
        prefix_map = {0: 1}
        curr_sum = 0
        count = 0

        for num in nums:
            curr_sum += num

            if (curr_sum - k) in prefix_map:
                count += prefix_map[curr_sum - k]

            prefix_map[curr_sum] = prefix_map.get(curr_sum, 0) + 1

        return count     