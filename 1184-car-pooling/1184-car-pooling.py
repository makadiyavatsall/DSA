class Solution(object):
    def carPooling(self, trips, capacity):
        max_pos = max(to for _, _, to in trips)
        diff = [0] * (max_pos + 1)

        for p, start, end in trips:
            diff[start] += p
            diff[end] -= p

        curr = 0
        for change in diff:
            curr += change
            if curr > capacity:
                return False
        return True
