class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum_price = float('inf')
        maximum_profit = 0

        for i in range(len(prices)):
            if prices[i] < minimum_price:
                minimum_price = prices[i]
            elif maximum_profit < prices[i] - minimum_price:
                maximum_profit = prices[i] - minimum_price
        
        return maximum_profit