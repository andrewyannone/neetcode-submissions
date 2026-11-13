class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lowest_price = prices[0]
        for i in prices:
            if i < lowest_price:
                lowest_price = i
            if i - lowest_price > max_profit:
                max_profit = i - lowest_price
        
        return max_profit
  

