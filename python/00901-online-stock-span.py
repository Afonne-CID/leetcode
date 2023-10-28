class StockSpanner:
    def __init__(self):
        self.stack = []  # Stack to store pairs (price, span)

    def next(self, price: int) -> int:
        span = 1  # Initialize the span to 1 by default

        # Check if we can increase the span by considering previous stock prices
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]

        # Add the current price and its span to the stack
        self.stack.append((price, span))

        return span

# Example usage:
stockSpanner = StockSpanner()
print(stockSpanner.next(100))  # Output: 1
print(stockSpanner.next(80))   # Output: 1
print(stockSpanner.next(60))   # Output: 1
print(stockSpanner.next(70))   # Output: 2
print(stockSpanner.next(60))   # Output: 1
print(stockSpanner.next(75))   # Output: 4
print(stockSpanner.next(85))   # Output: 6
