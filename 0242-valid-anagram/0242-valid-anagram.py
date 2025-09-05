class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        count = {}
        
        for ch in s:
            count[ch] = count.get(ch, 0) + 1
        
        for ch in t:
            if ch not in count:
                return False
            count[ch] -= 1
            if count[ch] == 0:
                del count[ch]
        
        return not count
