class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        left = 0
        max_profit = 0

        for right in range(n):
            while prices[left] > prices[right]:
                left += 1

            window_profit = prices[right] - prices[left]
            max_profit = max(window_profit, max_profit)

        return max_profit






     

        



            
        
        