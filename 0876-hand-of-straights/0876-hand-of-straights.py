from collections import Counter

class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)
        unique_cards = sorted(count.keys())
        
        for card in unique_cards:
            if count[card] > 0:
                group_count = count[card]
                
                for i in range(groupSize):
                    next_card = card + i
                    if count[next_card] < group_count:
                        return False  # Not enough consecutive cards
                    count[next_card] -= group_count

        return True
