class Solution(object):
    def combinationSum2(self, candidates, target):
        res = []
        candidates.sort()

        def backtrack(start, path, total):
            if total == target:
                res.append(list(path))
                return
            if total > target:
                return

            prev = -1
            for i in range(start, len(candidates)):
                if candidates[i] == prev:
                    continue  # skip duplicates at same depth
                path.append(candidates[i])
                backtrack(i + 1, path, total + candidates[i])
                path.pop()
                prev = candidates[i]

        backtrack(0, [], 0)
        return res

        