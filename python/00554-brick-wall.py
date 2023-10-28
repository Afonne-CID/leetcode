def leastBricks(wall):
    countGap = {0: 0}  # {Position: Gap count}

    for row in wall:
        total = 0  # Position
        for brick in row[:-1]:  # Exclude the last brick's width
            total += brick
            countGap[total] = 1 + countGap.get(total, 0)

    return len(wall) - max(countGap.values())
