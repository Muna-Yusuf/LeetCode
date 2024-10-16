from collections import Counter

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        occ_num ={}
        for num in arr:
            occ_num[num] = occ_num.get(num, 0) + 1

        count_values = Counter(occ_num.values())

        return all(count == 1 for count in count_values.values())
        
        
        