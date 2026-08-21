class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        Vowel = set("AEIOUaeiou")
        Win = s[:k]
        Sum = 0 
        Max = 0
        for i in range(k):
            if s[i] in Vowel:
                Max += 1
        Sum = Max
        for i in range(k,len(s)):
            if s[i] in Vowel and s[i-k] not in Vowel:
                Sum += 1
                Max = max(Max,Sum)
            elif s[i] not in Vowel and s[i-k] in Vowel:
                Sum -= 1
                Max = max(Max,Sum)
        return Max




        