def findCheapestPrice(n, flights, src, dst, k):
    # Initialize prices array with infinity
    prices = [float("inf")] * n
    prices[src] = 0  # Price to reach the source city is 0

    for i in range(k + 1):
        tempPrices = prices.copy()  # Create a temporary array to track updates

        for s, d, p in flights:  # s=source, d=destination, p=price
            if prices[s] == float("inf"):
                continue  # Skip cities that cannot be reached
            if prices[s] + p < tempPrices[d]:
                tempPrices[d] = prices[s] + p

        prices = tempPrices  # Update the main prices array

    return -1 if prices[dst] == float("inf") else prices[dst]
