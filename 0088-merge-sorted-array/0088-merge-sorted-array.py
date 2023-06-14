class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not nums1:
            nums1 = nums2
            return
        if not nums2:
            return
        i1 = 0
        i2 = 0
        while i1 < (m + i2) and i2 < n:
            if nums1[i1] <= nums2[i2]:
                i1 += 1
            else:
                nums1.insert(i1, nums2[i2])
                i2 += 1
        nums1[m + i2:] = nums2[i2:]