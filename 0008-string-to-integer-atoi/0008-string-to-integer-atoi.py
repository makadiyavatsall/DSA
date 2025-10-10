class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()  # Remove leading whitespaces
        if not s:
            return 0
        
        sign = 1
        i = 0
        
        # Check for sign
        if s[0] == '-':
            sign = -1
            i += 1
        elif s[0] == '+':
            i += 1
        
        result = 0
        # Convert digits
        while i < len(s) and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1
        
        result *= sign
        
        # Clamp within 32-bit signed integer range
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX
        
        return result
