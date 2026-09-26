class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minB=prices[0]
        maxP=0

        for p in prices:
            maxP=max(maxP, p-minB)
            if p<minB:
                minB=p
        return maxP