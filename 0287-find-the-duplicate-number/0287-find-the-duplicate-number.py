from collections import Counter

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = Counter(nums)
        
        for item, count in counts.items():
            if count > 1:
                return item