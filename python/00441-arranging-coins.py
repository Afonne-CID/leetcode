def arrangeCoins(n: int) -> int:
    left, right = 1, n
    result = 0

    while left <= right:
        mid = left + (right - left) // 2
        coins_needed = (mid * (mid + 1)) // 2

        if coins_needed == n:
            return mid
        elif coins_needed > n:
            right = mid - 1
        else:
            left = mid + 1
            result = max(mid, result)

    return result
