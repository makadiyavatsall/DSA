class Solution:
    def reverseVowels(self, s: str) -> str:
        left = 0
        right = len(s) - 1
        s_list = list(s)
        vowel = set("aeiouAEIOU")
        while left < right:
            if s_list[left] not in vowel:
                left += 1
            elif s_list[right] not in vowel:
                right -= 1
            else:
                s_list[left],s_list[right] = s_list[right],s_list[left]
                left += 1
                right -= 1
        return "".join(s_list)
        return "".join(s)   


    

        