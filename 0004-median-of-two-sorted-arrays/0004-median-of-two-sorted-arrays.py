class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:

        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)

        total = m + n
        half = (total + 1) // 2

        left, right = 0, m

        while left <= right:

            # Partition indexes
            mid1 = (left + right) // 2
            mid2 = half - mid1

            # Left and right values around partition
            L1 = float('-inf') if mid1 == 0 else nums1[mid1 - 1]
            R1 = float('inf') if mid1 == m else nums1[mid1]

            L2 = float('-inf') if mid2 == 0 else nums2[mid2 - 1]
            R2 = float('inf') if mid2 == n else nums2[mid2]

            # Correct partition
            if L1 <= R2 and L2 <= R1:

                # Odd total length
                if total % 2:
                    return max(L1, L2)

                # Even total length
                return (max(L1, L2) + min(R1, R2)) / 2

            # Move left
            elif L1 > R2:
                right = mid1 - 1

            # Move right
            else:
                left = mid1 + 1