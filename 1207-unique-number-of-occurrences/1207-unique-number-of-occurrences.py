class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq={}
        for num in arr:
            freq[num] = freq.get(num,0)+1
        seen = set()
        for count in freq.values():
            if count in seen:
                return False
            seen.add(count)
        return True