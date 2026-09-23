class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # choose a day, buy
        # choose a day, sell 
        # return max profit
        # prices array, prices[i] = prices of coin on ith day

        # if prices decreasing order, return 0, max_profit = 0

        max_profit = 0
        curr_min = prices[0]

        for price in prices:            
            curr_min = min(curr_min, price)
            curr_profit = price - curr_min
            max_profit = max(max_profit, curr_profit)
        return max_profit

