from collections import Counter

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dupli_num = set()
        for num in nums:
            if num in dupli_num:
                return num
            dupli_num.add(num)