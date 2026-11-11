class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        if prices:
            min_price = prices[0]


            for i in range(1 , len(prices)):
                
                curr = prices[i] - min_price

                min_price = min(min_price , prices[i])
                #print(curr)

                if max_profit < curr:
                    max_profit = curr
            
        return max_profit