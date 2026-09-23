class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # for max profit
        # we track the previous lowest and sell, see if each time has higher profit

        lowest = prices[0]
        # we initialize that the lowest price is the first day
        max_profit = 0
        # we also initialize the maximum profit to 0

        for price in prices:
            lowest = min(price, lowest)
            # track the lowest

            profit = price - lowest
            # profit = current price - lowest
            # find the maximum profit

            max_profit = max(max_profit, profit)
        return max_profit

        # dry run
        # prices = [10,1,5,6,7,1]
        # first loop, price = 10,l = 10, max = 0, profit = 0, max = 0
        # second loop, price = 1, l = 1, max =0, profit = 0, max =0
        # third loop, price = 5, l = 1, max = 0, profit = 4, max =4