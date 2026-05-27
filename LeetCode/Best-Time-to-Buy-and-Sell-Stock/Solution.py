1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        min_price = prices[0]
4        max_profit = 0
5
6        for i in range(1,len(prices)):
7            
8            price = prices[i]
9
10            if price < min_price:
11                min_price = price
12
13            profit = price - min_price
14
15            if profit > max_profit:
16                max_profit = profit
17            
18        return max_profit 