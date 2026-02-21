class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = ""

        first = strs[0]

        for i in range(len(first)):
            ch = first[i]

            for s in strs[1:]:
                if i >= len(s) or s[i] != ch:
                    return prefix

            prefix += ch

        return prefix