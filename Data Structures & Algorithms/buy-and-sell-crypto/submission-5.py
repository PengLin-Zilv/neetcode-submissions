class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # we want the lowest previous, loop over i, 
        # curren_price = price - lowerst

        # we say that the lowest is the first day  
        lowest = prices[0]
        # we will update the lowers

        # default 0
        max_profit = 0

        for price in prices:
            lowest = min(lowest, price)
            current_profit = price - lowest

            # update the profit
            max_profit = max(max_profit, current_profit)

        return max_profit
