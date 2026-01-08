class Solution:
    def isPalindrome(self, s: str) -> bool:   
        cleaned = ''.join(char.lower() for char in s if char.isalnum())
        is_palindrome = cleaned == cleaned[::-1]
        return is_palindrome
