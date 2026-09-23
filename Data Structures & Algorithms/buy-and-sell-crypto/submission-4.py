class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # the logic will be, the largest future - the lowest previous

        profit = 0
        current_min = prices[0]

        for price in prices:
            current_min = min(current_min, price)
            current_profit = price - current_min
            profit = max(profit, current_profit)

        return profit
            