class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []

        def backtrack(start, current, total):
            if total == target:
                res.append(list(current))
                return
            if total > target:
                return

            for i in range(start, len(candidates)):
                current.append(candidates[i])
                backtrack(i, current, total + candidates[i])  # reuse same number
                current.pop()  # backtrack step

        backtrack(0, [], 0)
        return res
