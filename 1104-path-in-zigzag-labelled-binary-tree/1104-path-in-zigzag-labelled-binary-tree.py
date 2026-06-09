class Solution:
    def pathInZigZagTree(self, label: int) -> list[int]:
        path = []

        while label >= 1:
            path.append(label)

            level = label.bit_length() - 1
            start = 2 ** level
            end = 2 ** (level + 1) - 1

            label = (start + end - label) // 2

        return path[::-1]