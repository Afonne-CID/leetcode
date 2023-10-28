def twoCitySchedCost(costs):
    diffs = []  # List to store cost differences
    for c1, c2 in costs:
        diffs.append([c2 - c1, c1, c2])

    diffs.sort()  # Sort the persons based on cost difference
    res = 0  # Initialize the total cost

    for i in range(len(diffs)):
        if i < len(diffs) // 2:
            res += diffs[i][2]  # Send to city B
        else:
            res += diffs[i][1]  # Send to city A

    return res
