class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if not prices:
            return 0

        left = 0 
        largest = 0

        for i in range(1, len(prices)):

            if prices[i] < prices[left]:
                left = i
            
            else:
                current = prices[i] - prices[left]
                if current > largest:
                    largest = current

        return largest