from collections import Counter

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        counts = Counter(nums)
        dupli = []

        for item, count in counts.items():
            if count > 1:
                dupli.append(item)

        for num in dupli:
            indices = [i for i, x in enumerate(nums) if x == num]
            for i in range(len(indices) - 1):
                if abs(indices[i] - indices[i + 1]) <= k:
                    return True
        
        return False