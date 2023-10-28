import heapq

def findMaximizedCapital(k, w, profits, capital):
    # Create a Max Heap for maximizing profits
    maxProfit = []

    # Create a Min Heap for minimizing capital requirements
    minCapital = [(c, p) for c, p in zip(capital, profits)]
    heapq.heapify(minCapital)

    for i in range(k):
        # Select projects with capital requirements we can afford
        while minCapital and minCapital[0][0] <= w:
            c, p = heapq.heappop(minCapital)
            # Add the negative of profit to Max Heap for maximizing profits
            heapq.heappush(maxProfit, -p)

        if not maxProfit:
            break

        # Take the project with the highest profit
        w += -1 * heapq.heappop(maxProfit)

    return w
