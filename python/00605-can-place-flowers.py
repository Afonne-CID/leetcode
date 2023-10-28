def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
    f = [0] + flowerbed + [0]

    for i in range(1, len(f) - 1):  # Skipping the first and last positions
        if f[i - 1] == 0 and f[i] == 0 and f[i + 1] == 0:
            f[i] = 1
            n -= 1
    return n <= 0
