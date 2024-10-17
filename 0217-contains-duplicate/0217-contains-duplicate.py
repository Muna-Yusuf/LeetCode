class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_dirc = {}
        
        for num in nums:
            nums_dirc[num] = nums_dirc.get(num, 0) + 1
        
        for num in nums_dirc.values():
            if num >= 2:
                return True
        
        
        return False
        