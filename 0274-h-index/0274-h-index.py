class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # Step 1: Sort citations in descending order
        citations.sort(reverse=True)

        h = 0

        # Step 2: Check how many papers have at least (i+1) citations
        for i in range(len(citations)):
            if citations[i] >= i + 1:
                h = i + 1
            else:
                break

        return h