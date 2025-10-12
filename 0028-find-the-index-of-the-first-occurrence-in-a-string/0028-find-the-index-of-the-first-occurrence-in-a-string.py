class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # Edge case: if needle is empty, return 0
        if not needle:
            return 0
        
        len_haystack = len(haystack)
        len_needle = len(needle)
        
        # Edge case: if needle is longer than haystack, it cannot be found
        if len_needle > len_haystack:
            return -1
            
        # Iterate through haystack to find potential starting positions of needle
        # The loop runs up to (len_haystack - len_needle) to ensure there's enough
        # length remaining for the needle.
        for i in range(len_haystack - len_needle + 1):
            # Check if the substring of haystack matches needle
            if haystack[i : i + len_needle] == needle:
                return i # Found the first occurrence
                
        # If the loop finishes, needle was not found
        return -1