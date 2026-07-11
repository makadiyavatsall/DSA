class Solution(object):
    def lengthOfLongestSubstring(self, s):
        Set = set()
        left= 0
        length = 0

        for right in range(len(s)):
            while s[right] in Set:
                Set.remove(s[left])
                left = left + 1

            Set.add(s[right])
            length = max(length,right - left + 1)
        return length
                                            
        
        