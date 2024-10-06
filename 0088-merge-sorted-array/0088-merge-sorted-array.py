class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        tem= nums1[:m]
        if len(nums1) >= len(nums2):
            nums1[:] = sorted(tem + nums2[:n])
        