import heapq

class MedianFinder:

    def __init__(self):
        # Max heap (store negatives)
        self.left = []
        # Min heap
        self.right = []

    def addNum(self, num: int) -> None:
        # Step 1: push into max heap
        heapq.heappush(self.left, -num)

        # Step 2: move largest from left to right
        heapq.heappush(self.right, -heapq.heappop(self.left))

        # Step 3: balance sizes
        if len(self.right) > len(self.left):
            heapq.heappush(self.left, -heapq.heappop(self.right))

    def findMedian(self) -> float:
        # Odd number of elements
        if len(self.left) > len(self.right):
            return -self.left[0]
        # Even number of elements
        return (-self.left[0] + self.right[0]) / 2
