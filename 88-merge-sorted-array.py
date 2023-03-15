def mergeSorted(nums1, nums2, m, n):
    for i in range(m + n):
        if nums2 == []:
            break
        if i == m + n - 1:
            nums1 = nums1[: m + n - 1] + nums2
            break
        if nums2[0] <= nums1[i]:
            nums1 = nums1[:i] + [nums2[0]] + nums1[i:]
            nums2 = nums2[1:]
            n -= 1
    return nums1


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
print(mergeSorted(nums1, nums2, m, n))
