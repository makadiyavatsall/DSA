class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()

        ans = 0

        for house in houses:
            idx = bisect_left(heaters, house)

            left = float('inf')
            right = float('inf')

            if idx > 0:
                left = house - heaters[idx - 1]

            if idx < len(heaters):
                right = heaters[idx] - house

            ans = max(ans, min(left, right))

        return ans
        