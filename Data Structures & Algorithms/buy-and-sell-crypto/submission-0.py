class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        yesterday = prices[0]
        for i in range(1,len(prices)):
            today = prices[i]
            if today < yesterday :
                yesterday = today
            else:
                profit = today - yesterday
                max_profit = max(max_profit, profit )
        return max_profit 

