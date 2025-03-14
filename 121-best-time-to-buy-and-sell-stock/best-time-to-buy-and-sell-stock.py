class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=prices[0]
        profit=0
        n=len(prices)
        for i in range(1,n):
            mini=min(mini,prices[i])
            profit=max(profit,prices[i]-mini)
        return profit
        