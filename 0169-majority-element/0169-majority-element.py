class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count_map = {}
        
        for num in nums:
            if num in count_map:
                count_map[num] += 1
            else:
                count_map[num] = 1
        
        # Find the element with count greater than n // 2
        for num, count in count_map.items():
            if count > len(nums) // 2:
                return num