class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # for maxProfit, we want buy low sell high
        # for each price day, we record the lowest
        # see if we sell them today, how much we earn

        max_profit = 0
        min_price = prices[0]
        # price = price - min_price

        for price in prices:
            min_price = min(price, min_price)

            profit = price - min_price

            max_profit = max(max_profit, profit)
        return max_profit