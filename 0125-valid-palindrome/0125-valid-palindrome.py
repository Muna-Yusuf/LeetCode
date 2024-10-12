class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        join_all = ''.join(char for char in s.lower() if char.isalnum())
        return join_all == join_all[::-1]

        

        