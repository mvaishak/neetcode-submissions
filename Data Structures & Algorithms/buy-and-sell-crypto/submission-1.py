class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mx_p = 0
        buy = prices[0]
        for i in range(1,len(prices)):
            cur = prices[i]
            p = cur - buy
            mx_p = max(mx_p,p)
            buy = min(buy,cur)
        return mx_p
        