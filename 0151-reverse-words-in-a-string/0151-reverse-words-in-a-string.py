class Solution:
    def reverseWords(self, s: str) -> str:
        new=[]
        s=s.split()
        for i in s:
            new.append(i)
        res=""
        for i in range(len(new)-1,-1,-1):
            res+=new[i]
            res+=" "        
        return res.rstrip()