class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        order_map = {char: index for index, char in enumerate(order)}
        
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            # Compare the words character by character
            for j in range(min(len(word1), len(word2))):
                char1_index = order_map[word1[j]]
                char2_index = order_map[word2[j]]
                
                if char1_index < char2_index:
                    break
                elif char1_index > char2_index:
                    return False
            else:
                if len(word1) > len(word2):
                    return False

        return True