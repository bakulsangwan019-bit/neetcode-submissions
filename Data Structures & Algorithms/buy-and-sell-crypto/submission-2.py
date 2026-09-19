class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0 
        right = 1
        largest = 0

        while right < len(prices):

            if prices[left] < prices[right]:
                current = prices[right] - prices[left]

                if current > largest:
                    largest = current
            
            else:
                left = right

            right += 1
        
        return largest
        
