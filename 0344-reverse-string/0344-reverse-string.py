class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        n = len(s)
        rev = [''] * n

        for i in range(n):
            rev[i] = s[n - 1 - i]

        for i in range(n):
            s[i] = rev[i]
