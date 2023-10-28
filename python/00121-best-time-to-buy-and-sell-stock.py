def maxProfit(self, prices: List[int]) -> int:
    # Initialize pointers and max profit
    left = 0
    right = 1
    maxProfit = 0
    
    # Iterate through prices
    while right < len(prices):
        # Calculate profit
        profit = prices[right] – prices[left]
        
        # Update max profit if necessary
        maxProfit = max(maxProfit, profit)
        
        # Check if it’s a profitable transaction
        if prices[right] < prices[left]:
            left = right
        
        # Move right pointer
        right += 1
    
    return maxProfit
