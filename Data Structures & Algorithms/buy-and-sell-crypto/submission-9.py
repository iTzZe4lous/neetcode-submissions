class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit=0
        buy, sell= 0, 1
        while sell in range(len(prices)):
            if prices[sell]<prices[buy]:
                buy=sell
            maxProfit=max(maxProfit, prices[sell]-prices[buy])
            sell+=1
        return maxProfit
