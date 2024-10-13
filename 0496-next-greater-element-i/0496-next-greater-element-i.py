class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        output = []
        
        for i in nums1:
            index = nums2.index(i)
            value = -1
            for j in range (index + 1, len(nums2)):
                if nums2[j] > i:
                    value = nums2[j]
                    break
            output.append(value)
        return output
        