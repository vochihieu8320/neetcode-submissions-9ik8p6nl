class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0

        for i in range(n):
            price = prices[i]

            left = i + 1

            future_price = 0
            while left < n:
                future_price = prices[left] if prices[left] > future_price else future_price
                left += 1

            profit = future_price - price
            if profit <= 0: continue

            max_profit = max(profit, max_profit)

        return max_profit


     

        



            
        
        