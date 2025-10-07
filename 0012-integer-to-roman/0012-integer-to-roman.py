class Solution(object):
    def intToRoman(self, num):
        val = [1000, 900, 500, 400,
               100, 90, 50, 40,
               10, 9, 5, 4, 1]
        
        syms = ["M", "CM", "D", "CD",
                "C", "XC", "L", "XL",
                "X", "IX", "V", "IV", "I"]
        
        res = ""
        i = 0
        
        while num > 0:
            count = num // val[i]          # how many times current value fits
            res += syms[i] * count         # add symbol that many times
            num -= val[i] * count          # subtract that part from number
            i += 1                         # move to next smaller value
            
        return res
