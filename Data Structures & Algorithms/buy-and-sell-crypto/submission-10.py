class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # window valid: the other value need to greater than left
        # we need find maximum distance in window
        n = len(prices)
        left = 0
        right = left + 1
        window_distance = 0

        while left < n and right < n:
            if prices[left] < prices[right]:
                profix = prices[right] - prices[left]
                window_distance = max(profix, window_distance)
                right += 1
            else:
                left = right
                right = left + 1
                
        return window_distance



     

        



            
        
        