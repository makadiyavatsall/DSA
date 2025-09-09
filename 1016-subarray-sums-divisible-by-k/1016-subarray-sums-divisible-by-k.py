class Solution(object):
    def subarraysDivByK(self, nums, k):
        count = 0
        prefixSum = 0
        freq = {0: 1}   
        
        for num in nums:
            prefixSum += num
            remainder = prefixSum % k
            
            
            if remainder < 0:
                remainder += k
            
            if remainder in freq:
                count += freq[remainder]
            
            
            freq[remainder] = freq.get(remainder, 0) + 1
        
        return count
