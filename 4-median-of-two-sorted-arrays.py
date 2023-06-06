from typing import List, Optional


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        midpoint = (m + n) // 2
        if m == 0:
            if (m + n) % 2 == 0 and not midpoint == 0:
                return (nums2[midpoint - 1] + nums2[midpoint]) / 2
            else:
                return nums2[midpoint]
        if n == 0:
            if (m + n) % 2 == 0 and not midpoint == 0:
                return (nums1[midpoint - 1] + nums1[midpoint]) / 2
            else:
                return nums1[midpoint]
        i, j = 0, 0
        incI = True
        while i + j < midpoint:
            if i == m:
                j += 1
            if j == n:
                i += 1
            else:
                if nums1[i] < nums2[j]:
                    i += 1
                elif nums1[i] > nums2[j]:
                    j += 1
                elif nums1[i] == nums2[j]:
                    if incI:
                        i += 1
                        incI = False
                    else:
                        j += 1
                        incI = True
        if i == m:
            i = m - 1
        if j == n:
            j = n - 1
        if (m + n) % 2 == 0:
            return (nums1[i] + nums2[j]) / 2
        else:
            if nums1[i] < nums2[j]:
                return nums1[i]
            else:
                return nums2[j]


s = Solution()
print(s.findMedianSortedArrays([1, 3, 5], [2, 7, 9]))

# [2, 4, 6] [1, 3, 9]
#  i         j         i+j = 0
#  i            j      i+j = 1
#     i         j      i+j = 2
#     i            j   i+j = 3
# [1, 2, 3, 4, 6, 9]
