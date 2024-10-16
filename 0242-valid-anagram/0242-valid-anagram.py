class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len (t):
            return False
        
        map_char = {}

        for char in s:
            map_char[char] = map_char.get(char, 0) + 1

        for char in t:
            if char not in map_char or map_char[char] == 0:
                return False
            else:
                map_char[char] -= 1
        return all(char == 0 for char in map_char.values())
