class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)-1
        i, j = 0, n
        volume = 0
        while i != j:
            if height[i] > height[j]:
                v = height[j] * n
                volume = max(volume, v)
                n -= 1
                j -= 1
            else:
                v = height[i] * n
                volume = max(volume, v)
                n -= 1
                i += 1
        return volume
