class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        min_price = float('inf')  # Initialize min price to a large value
        max_profit = 0  # Initialize max profit to 0

        for price in prices:
            # Update the minimum price
            if price < min_price:
                min_price = price
            
            # Calculate potential profit
            profit = price - min_price
            
            # Update maximum profit if the potential profit is higher
            if profit > max_profit:
                max_profit = profit

        return max_profit  # Ensure this is indented properly inside the method
