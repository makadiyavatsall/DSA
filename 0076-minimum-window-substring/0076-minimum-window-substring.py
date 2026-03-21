class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        need = {}
        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        window = {}
        left = 0
        have = 0
        need_count = len(need)

        res = [-1, -1]
        res_len = float("inf")

        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1

            if char in need and window[char] == need[char]:
                have += 1

            while have == need_count:
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1

                window[s[left]] -= 1
                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1

                left += 1

        l, r = res
        return s[l:r+1] if res_len != float("inf") else ""