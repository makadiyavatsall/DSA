class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        prefix_map = {0: 1}
        curr_sum = 0
        count = 0

        for num in nums:
            curr_sum += num
            mod = curr_sum % k

            if mod in prefix_map:
                count += prefix_map[mod]

            prefix_map[mod] = prefix_map.get(mod, 0) + 1

        return count