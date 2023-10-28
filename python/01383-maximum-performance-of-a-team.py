def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
    mod = 10 ** 9 + 7
    eng = []

    # Combine efficiency and speed into pairs and sort by efficiency in descending order
    for eff, spd in zip(efficiency, speed):
        eng.append([eff, spd])
    eng.sort(reverse=True)

    res, speed = 0
    minHeap = []

    for eff, spd in eng:
        if len(minHeap) == k:
            speed -= heapq.heappop(minHeap)
        speed += spd
        heapq.heappush(minHeap, spd)
        res = max(res, eff * speed)

    return res % mod
