class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)
        s = list(s)
        t = list(t)
        if len(s) != len(t):
            return False
        
        for letter in s:
            if letter in t:
                t.remove(letter)
            else:
                return False
        return True