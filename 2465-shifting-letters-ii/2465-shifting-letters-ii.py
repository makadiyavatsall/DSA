class Solution(object):
    def shiftingLetters(self, s, shifts):
        n = len(s)
        diff = [0] * (n + 1)   # difference array

        # Build the difference array
        for start, end, direction in shifts:
            val = 1 if direction == 1 else -1
            diff[start] += val
            if end + 1 < len(diff):
                diff[end + 1] -= val

        # Prefix sum to get net shifts for each index
        for i in range(1, n):
            diff[i] += diff[i - 1]

        # Apply shifts
        res = []
        for i, ch in enumerate(s):
            shift = diff[i] % 26   # wrap around
            new_char = chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
            res.append(new_char)

        return "".join(res)
