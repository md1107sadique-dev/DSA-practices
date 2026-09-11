class Solution(object):
    def maxProfit(self, prices):
        max_profit = 0
        n = len(prices)
        
        # m-1(Brute Force)
        # for i in range(n):
        #     buy = prices[i]
        #     for j in range(i+1,n):
        #         profit = prices[j] - buy
        #         if max_profit < profit:
        #             max_profit = profit
        # return max_profit

        # m-2(optimal)
        minimum = prices[0]
        for i in range(n):
            if prices[i] < minimum:
                minimum = prices[i]
            sell = prices[i] - minimum
            if sell > max_profit:
                max_profit = sell
        return max_profit

        